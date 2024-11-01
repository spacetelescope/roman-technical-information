# Roman Observatory Slew and Settle Times

Slew duration and the slew profile are determined by the slew length, the maximum allowed rate, and the maximum allowed acceleration. The maximum allowed rate is fixed (by observatory safing constraints). The maximum allowed acceleration is determined by the torque authority of the reaction wheels and the moment of inertia of the observatory. The torque is slightly different in the direction of the long axis of the WFI FoV than the short axis. For the purpose of estimating survey efficiency, slew times in the diagonal direction is a reasonable approximation.

Slews are acceleration limited if the rate does not reach the maximum value, and rate-limited for longer slews (>~1deg) where the maximum rate is achieved. Since the maximum allowed rate is fixed, improvements in torque authority primarily improve the performance of short slews. Roman's core community surveys are dominated by short slews.

Sharp changes in acceleration may excite structural or slosh oscillations that could adversely affect settling time. To avoid this, a shaped profile is computed onboard to avoid sharp acceleration discontinuities. More details can be found in [Stoneking et al 2017](https://ntrs.nasa.gov/citations/20170001037).

The times for some example telescope slews are presented in the table below. These include settling time. These assume 1.566 Nm max torque, and MOI of 40,000 kg m<sup>2</sup>.

| Slew Type | Slew Angle (deg) | Slew and Settle Time (s) |
|-----------|------------------|---------------|
| Gap Fill  | 0.025            | 18.9          |
| Short FoV | 0.4              | 39.3          |
| Long FoV  | 0.8              | 52.5          |
| 2-deg     | 2.0              | 77.8          |
| 5-deg     | 5.0              | 141           |
| 10-deg    | 10.0             | 246           |
| 30-deg    | 30.0             | 646           |
| 90-deg    | 90.0             | 1844          |

## Included files

| Filename| Description|
|---------|------------|
| SlewSettle.ecsv              | Slew and settle times as a function of slew distance                          |
| example_telescope_slews.yaml | Example slew types/angles and associated slew and settle times in YAML format |
