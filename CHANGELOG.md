
### 1.0.4 (RC1): Picard
* Defaults changes:
  * Anti-gravity is now off by default. Anti-gravity was a bandaid for improper filtering. Because of that, AG has no effect with IMU-F. In certain cases, AG would negatively impact flight performance with IMU-F.
  * Default pid loop and gyro loop is now 32K.
  * Default F4 clock speed is now 192MHZ. This is because Multishot runs better with the clock speed as a multiple of 32. You can set it to 168MHZ and things will still run fine, but 192 is preferred because of maths.
  * note: Proshot1000 is supported in the 32.4 BLHELI_32 firmware. Proshot1000 is preferred over Dshot1200. Because of BeF/BuF codes, Dshot600/1200 are incompatible with rc_interpolation enabled at 32K without overclocking to 216MHZ. if you select DSHOT1200, rc_interpolation is not OFF, and the pid loop is 32k, we will automatically set overclock to 216MHZ. You can also lower the pid loop to 16K if you prefer to not overclock.
* add imuf_rate setting. Accepted values: 32K, 16K, 8K, 4K, 2K, 1K. Use this to match your gyro loop speed.
```
//default:
set imuf_rate = 32K #this should match your gyro loop time.
```
* replace imuf_AXIS_r with imuf_AXIS_w. This is similar to the previous "dyn_gain" setting except applies directly to our fully dynamic Kalman implementations and is applied per-axis. Accepted values: 0 - 199. Default: 6(min). 106+ is an alternative Dynamic Kalman we are also testing. Once we have determined which is the most appropriate for the majority of users, we will be simplifying this option.

```
//default:
set imuf_pitch_w = 10
set imuf_roll_w = 10
set imuf_yaw_w = 10
//alternate filtering method with wider dynamic gain value:
set imuf_pitch_w = 115
set imuf_roll_w = 115
set imuf_yaw_w = 115
```
* Known issue: When Using Dshot1200 & 32k pid loop, if accelerometer is OFF, CPU usage goes to 100%. Leave accelerometer on in this instance. This does not seem to affect other protocols.

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
