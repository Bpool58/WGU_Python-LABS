num_resistors = 5
resistors = []
voltage_drop = []

print(f'{num_resistors} resistors are in series.')
print('This program calculates the voltage drop across each resistor.')
input_voltage = float(input('Input voltage applied to circuit: '))
print(input_voltage)

print(f'Input ohms of {num_resistors} resistors:')
for i in range(num_resistors):
    res = float(input(f'{i + 1} '))
    print(res)
    resistors.append(res)

current = input_voltage / sum(resistors)

for r in resistors:
    drop = current * r # Ohms's Law: V = I * R
    voltage_drop.append(drop)

print('\nVoltage drop across each resistor:')
for i in range(num_resistors):
    print(f'Resistor: {i + 1}: {voltage_drop[i]:.2f} V')
