
### 1.0.4 (BETA): Picard
* add imuf_rate setting. Accepted values: 32K, 16K, 8K, 4K, 2K, 1K. Use this to match your gyro loop speed. Default: 16K
* replace imuf_AXIS_r with imuf_AXIS_w. This is similar to the previous "dyn_gain" setting except applies directly to our fully dynamic Kalman implementations and is applied per-axis. Accepted values: 0 - 199. Default: 6(min). 106+ is an alternative Dynamic Kalman we are also testing. Once we have determined which is the most appropriate for the majority of users, we will be simplifying this option.


```
//default:
set imuf_pitch_w = 6
set imuf_roll_w = 6
set imuf_yaw_w = 6
//alternate filtering method with wider dynamic "window":
set imuf_pitch_w = 115
set imuf_roll_w = 115
set imuf_yaw_w = 115
```
* Butterflight: New Dshot driver which can run correctly with a 32K PID loop without overclocking. 
For now, if you need to run dshot at 32K apply the following in the CLI:

```
set dterm_filter_style=KD_FILTER_NOSP
set pid_process_denom=1
set gyro_sync_denom=1
set imuf_rate = 32K
set acc_hardware = NONE
set cpu_overclock = 216MHZ
set motor_pwm_protocol = DSHOT1200 (DSHOT600 at 32k will corrupt. It is a specification limitiation)
```

### 1.0.3: Bacon & Spam
* fix init bug where the quad wouldn't arm randomly in very rare instances.
* remove imuf_dyn_gain as it created MTO in more instances than solved. Most suggestions were to turn it off in general.

### 1.0.2: Sausage
* add auto-update, remove the need for "imufupdate" in console
* fix imuf_dyn_gain scaling

### 1.0.1: Waffles
* fix for imuf_dyn_gain 

### 1.0.0: Pancake Batter (Initial Release)
* Party Parrots Everywhere.
