import matplotlib.pyplot as plt
import numpy as np

sensor_x, sensor_y = 0, 0
target_x, target_y = 0.5, 2  # You can change target_y to move the dot


plt.plot([-1,1], [0,0], 'k-', linewidth=2, label='Ground')

plt.plot([target_x, target_x], [1, 3], 'b-', linewidth=2, label='Target')
plt.text(target_x + 0.1, 2, 'Pantograph Range', rotation=90, va='center', color='blue')

plt.plot(sensor_x, sensor_y, 'ro', markersize=10, label='Sensor')

plt.plot(target_x, target_y, 'go', markersize=10, label='Target Point')

plt.plot([sensor_x, target_x], [sensor_y, target_y], 'g--', label='Distance')

distance = np.sqrt((target_x - sensor_x) ** 2 + (target_y - sensor_y) ** 2)
plt.text(((sensor_x + target_x) / 2)-0.12, (sensor_y + target_y) / 2, f"{distance:.2f} m", color='green', fontsize=10, ha='center')

# Calculate angle in degrees (between line and horizontal)
dx = target_x - sensor_x
dy = target_y - sensor_y
angle_rad = np.arctan2(dy, dx)
angle_deg = np.degrees(angle_rad)

plt.text(sensor_x+0.15, sensor_y+0.05, f"{angle_deg:.2f}°", color='purple', fontsize=10, ha='center')

plt.xlabel('Horizontal distance (m)')
plt.ylabel('Height (m)')
plt.title('Sensor and Pantograph Placement')
plt.grid(True)
plt.show()