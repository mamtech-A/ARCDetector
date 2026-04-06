import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sensor_x, sensor_y = 0, 0
target_x, target_y = 1, 2  # You can change target_y to move the dot


plt.plot([-0.5,1.5], [0,0], 'k-', linewidth=2, label='Ground')

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

plt.text(sensor_x+0.15, sensor_y+0.05, f"{angle_deg:.1f}°", color='purple', fontsize=10, ha='center')

mid_y=2
target_y_start = 1
target_y_end = 3
dot_ys = [mid_y]
step = 0.5
# Go upwards from midpoint
y = mid_y + step
while y <= target_y_end:
    dot_ys.append(y)
    y += step

# Go downwards from midpoint
y = mid_y - step
while y >= target_y_start:
    dot_ys.append(y)
    y -= step
dot_ys = sorted(dot_ys)


for y in dot_ys:
    plt.plot(target_x, y, 'go', markersize=8)
    # Calculate distance
    distance = np.sqrt((target_x - sensor_x) ** 2 + (y - sensor_y) ** 2)
    # Calculate angle to ground
    dx = target_x - sensor_x
    dy = y - sensor_y
    angle_rad = np.arctan2(dy, dx)
    angle_deg_other_point = np.degrees(angle_rad)
    sensitivity_df = pd.read_csv(r'C:\Users\Mamtech\Documents\pantohealth\arc\fov-sensitivity\sensitivity.csv', header=None, names=['angle', 'sensitivity'])    
    angle_diff = int(round(angle_deg_other_point - angle_deg))
    nearest_idx = (sensitivity_df['angle'] - angle_diff).abs().idxmin()
    sensitivity = sensitivity_df.loc[nearest_idx, 'sensitivity']    # Annotate distance and angle
    plt.text(target_x + 0.2, y, f"{distance:.2f}m (Distance to sensor)\n{(angle_deg_other_point-angle_deg):.1f}° (Sensitivity: {sensitivity})", va='center', fontsize=8, color='green')





plt.xlabel('Horizontal distance (m)')
plt.ylabel('Height (m)')
plt.title('Sensor and Pantograph Placement')
plt.grid(True)
plt.show()