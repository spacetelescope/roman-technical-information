Slew and Settle Times
--

Slew duration and the slew profile are determined by the slew length, the maximum allowed rate, and the maximum allowed acceleration. The maximum allowed rate is fixed (by observatory safing constraints). The maximum allowed acceleration is determined by the torque authority of the reaction wheels and the moment of inertia of the observatory. The torque is slightly different in the direction of the long axis of the WFI FoV than the short axis. For the purpose of estimating survey efficiency, slew times in the diagonal direction is a reasonable approximation.

Slews are acceleration limited if the rate does not reach the maximum value, and rate-limited for longer slews (>~1deg) where the maximum rate is achieved. Since the maximum allowed rate is fixed, improvements in torque authority primarily improve the performance of short slews. Roman's core community surveys are dominated by short slews.

Sharp changes in acceleration may excite structural or slosh oscillations that could adversely affect settling time. To avoid this, a shaped profile is computed onboard to avoid sharp acceleration discontinuities. More details can be found in Stoneking et al 2017.

The times for some example telescope slews are presented in the table below. These include settling time. These assume 1.566 Nm max torque, and MOI of 40,000 kg-m^2

| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
