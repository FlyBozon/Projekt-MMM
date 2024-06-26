import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth
from PIL import Image, ImageTk

def update_fraction():
    try:
        J1 = float(J1_entry.get())
        n1 = float(n1_entry.get())
        n2 = float(n2_entry.get())
        J2 = float(J2_entry.get())
        b = float(b_entry.get())
        k = float(k_entry.get())
    except ValueError:
        messagebox.showerror("Blad", "Wprowadź poprawnie всі liczby")

def plot_response():
    try:
        J1 = float(J1_entry.get())
        n1 = float(n1_entry.get())
        n2 = float(n2_entry.get())
        J2 = float(J2_entry.get())
        b = float(b_entry.get())
        k = float(k_entry.get())
        
        selected = var.get()
        T = float(time_entry.get())
        amplitude = float(amplitude_entry.get())
        
        fig, axs = plt.subplots(2, 2, figsize=(10, 8))
        time_values = np.linspace(0, T, 10000)
        
        if selected == 1:
            frequency = float(frequency_entry.get())
            phase = float(phase_entry.get())
            signal = amplitude * np.sin(2 * np.pi * frequency * time_values + np.deg2rad(phase))
        elif selected == 2:
            signal = amplitude * np.heaviside(time_values, 1)
        elif selected == 3:
            frequency = float(frequency_entry.get())
            signal = amplitude * sawtooth(2 * np.pi * frequency * time_values, 0.5)
        elif selected == 4:
            signal = amplitude * np.ones_like(time_values)
        
        axs[0, 0].plot(time_values, signal)
        axs[0, 0].set_title("Pobudzenie")
        axs[0, 0].set_xlabel("Czas [s]")
        axs[0, 0].set_ylabel("Amplituda")
        axs[0, 0].grid(True)

        axs[1, 0].set_title("Pozycja [rad]")

        def derivative(y, t, Tm):
            theta2, omega2 = y
            dx1_dt = omega2
            dx2_dt = (Tm * (n2 / n1) - b * omega2 - k * theta2) / (J2 + J1 * (n2 / n1))
            return np.array([dx1_dt, dx2_dt])

        y0 = [0, 0]
        dt = T / 10000
        y = np.zeros((len(time_values), len(y0)))
        y[0] = y0
        for i in range(1, len(time_values)):                               
            Tm = signal[i]  
            k1 = derivative(y[i-1], time_values[i-1], Tm)                       
            k2 = derivative(y[i-1] + 0.5*dt*k1, time_values[i-1] + 0.5*dt, Tm)
            k3 = derivative(y[i-1] + 0.5*dt*k2, time_values[i-1] + 0.5*dt, Tm)
            k4 = derivative(y[i-1] + dt*k3, time_values[i-1] + dt, Tm)
            y[i] = y[i-1] + dt*(k1 + 2*k2 + 2*k3 + k4) / 6

        axs[1, 0].plot(time_values, y[:, 0], color='orange', label='Runge-Kutta')
        axs[1, 0].set_xlabel("Czas [s]")
        axs[1, 0].set_ylabel("Pozycja [rad]")
        axs[1, 0].grid(True)

        y_euler = np.zeros((len(time_values), len(y0)))
        y_euler[0] = y0
        for i in range(1, len(time_values)):
            Tm = signal[i]  
            y_euler[i] = y_euler[i-1] + dt * derivative(y_euler[i-1], time_values[i-1], Tm)

        axs[1, 0].plot(time_values, y_euler[:, 0], color='blue', linestyle='--', label='Euler')
        axs[1, 0].legend()

        axs[0, 1].plot(time_values, y[:, 1], color='green', label='Runge-Kutta')
        axs[0, 1].plot(time_values, y_euler[:, 1], color='purple', linestyle='--', label='Euler')
        axs[0, 1].set_title("Szybkość [rad/s]")
        axs[0, 1].set_xlabel("Czas [s]")
        axs[0, 1].set_ylabel("Szybkość [rad/s]")
        axs[0, 1].grid(True)
        axs[0, 1].legend()

        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawnie wszystkie liczby")

def load_and_display_image(frame, image_path):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(frame, image=photo)
    label.image = photo
    label.pack()

def main():
    window = tk.Tk()
    window.title("Model")
    window.geometry("800x600")

    canvas = tk.Canvas(window)
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    input_frame = tk.Frame(scrollable_frame)
    input_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nw')

    global J1_entry, n1_entry, n2_entry, J2_entry, b_entry, k_entry
    tk.Label(input_frame, text="J1:", font=("Helvetica", 14)).grid(row=0, column=0, sticky='e')
    J1_entry = tk.Entry(input_frame)
    J1_entry.grid(row=0, column=1, sticky='w')

    tk.Label(input_frame, text="n1:", font=("Helvetica", 14)).grid(row=1, column=0, sticky='e')
    n1_entry = tk.Entry(input_frame)
    n1_entry.grid(row=1, column=1, sticky='w')

    tk.Label(input_frame, text="n2:", font=("Helvetica", 14)).grid(row=2, column=0, sticky='e')
    n2_entry = tk.Entry(input_frame)
    n2_entry.grid(row=2, column=1, sticky='w')

    tk.Label(input_frame, text="J2:", font=("Helvetica", 14)).grid(row=3, column=0, sticky='e')
    J2_entry = tk.Entry(input_frame)
    J2_entry.grid(row=3, column=1, sticky='w')

    tk.Label(input_frame, text="b:", font=("Helvetica", 14)).grid(row=4, column=0, sticky='e')
    b_entry = tk.Entry(input_frame)
    b_entry.grid(row=4, column=1, sticky='w')

    tk.Label(input_frame, text="k:", font=("Helvetica", 14)).grid(row=5, column=0, sticky='e')
    k_entry = tk.Entry(input_frame)
    k_entry.grid(row=5, column=1, sticky='w')

    update_button = tk.Button(input_frame, text="Aktualizuj dane", command=update_fraction)
    update_button.grid(row=6, columnspan=2)

    global time_entry, amplitude_entry, frequency_entry, phase_entry, var
    time_label = tk.Label(input_frame, text="Czas pobudzenia [s]:", font=("Helvetica", 10))
    time_label.grid(row=7, column=0, sticky='e', padx=20, pady=10)
    time_entry = tk.Entry(input_frame)
    time_entry.grid(row=7, column=1, sticky='w', padx=20, pady=10)

    tk.Label(input_frame, text="Rodzaj pobudzenia:", font=("Helvetica", 10)).grid(row=8, column=0, sticky='e', padx=20, pady=10)
    var = tk.IntVar(value=2)
    tk.Radiobutton(input_frame, text="Sinusoida", variable=var, value=1, font=("Helvetica", 10)).grid(row=8, column=1, sticky='w', padx=20, pady=10)
    tk.Radiobutton(input_frame, text="Skok jednostkowy", variable=var, value=2, font=("Helvetica", 10)).grid(row=9, column=1, sticky='w', padx=20, pady=10)
    tk.Radiobutton(input_frame, text="Trojkatne", variable=var, value=3, font=("Helvetica", 10)).grid(row=10, column=1, sticky='w', padx=20, pady=10)
    tk.Radiobutton(input_frame, text="Prostokątne", variable=var, value=4, font=("Helvetica", 10)).grid(row=11, column=1, sticky='w', padx=20, pady=10)

    amplitude_label = tk.Label(input_frame, text="Amplituda:", font=("Helvetica", 10))
    amplitude_label.grid(row=12, column=0, sticky='e', padx=20, pady=10)
    amplitude_entry = tk.Entry(input_frame)
    amplitude_entry.grid(row=12, column=1, sticky='w', padx=20, pady=10)

    frequency_label = tk.Label(input_frame, text="Częstotliwość [Hz] (dla sinusoidy i trojkatnego):", font=("Helvetica", 10))
    frequency_label.grid(row=13, column=0, sticky='e', padx=20, pady=10)
    frequency_entry = tk.Entry(input_frame)
    frequency_entry.grid(row=13, column=1, sticky='w', padx=20, pady=10)

    phase_label = tk.Label(input_frame, text="Faza w stopniach (dla sinusoidy):", font=("Helvetica", 10))
    phase_label.grid(row=14, column=0, sticky='e', padx=20, pady=10)
    phase_entry = tk.Entry(input_frame)
    phase_entry.grid(row=14, column=1, sticky='w', padx=20, pady=10)

    plot_button = tk.Button(input_frame, text="Wykreśl odpowiedź", command=plot_response)
    plot_button.grid(row=15, column=1, sticky='w', padx=20, pady=10)

    image_frame = tk.Frame(scrollable_frame)
    image_frame.grid(row=0, column=1, padx=20, pady=20, sticky='nw')
    load_and_display_image(image_frame, "./scheme.png")

    window.mainloop()

if __name__ == "__main__":
    main()
