
### 1.0.5 (RC5): Picard
* Defaults changes:
  * Default gyro and pid loop is 16k
  * note: The reason for this is people with 8 bit ESCs would attempt to set dshot600 as their protocol and it wouldn't arm. Dshot600 won't run at 32k. Only Dshot1200 will run properly at 32k and only on 32 bit ESCs. Proshot is not ready for prime-time. People have reported desyncs and death rolls using pro-shot. This is an implementation problem in BeF/BuF/blheli_32. Also, Dshot600/1200 are incompatible with rc_interpolation enabled at 32K without overclocking to 216MHZ. if you select DSHOT1200, rc_interpolation is not OFF, and the pid loop is 32k, we will automatically set overclock to 216MHZ. You can also leave the pid loop to 16K if you prefer to not overclock.
  * Default protocol is Multishot
  * Default F4 clock speed is now 192MHZ. This is because Multishot runs better with the clock speed as a multiple of 32. You can set it to 168MHZ and things will still run fine, but 192 is preferred because of maths.
  * Default pids are now back down to 3.4.2 defaults. BeF pids were just way too high for practically anything running our board.
  * Default Anti-gravity gain is now 3 and antigravity feture is enabled by default. Mileage may vary. In some cases, it can help with stability, but with a gain of 5 (previous default) or 8+, it was causing oscillations rather than fixing them.
* add imuf_rate setting. Accepted values: 32K, 16K, 8K, 4K, 2K, 1K. Use this to match your gyro loop speed. 
  * NOTE: It is automatically kept in sync with the gyro speed dropdown as of RC2.
* CLI: "version" now tells you what IMUF version you are running.
* Configurator: You are now able to flash via the dropdown in the UI. :party_parrot:
* replace imuf_AXIS_r with imuf_AXIS_w. This is similar to the previous "dyn_gain" setting except applies directly to our fully dynamic Kalman implementations and is applied per-axis. Accepted values: 0 - 199. Default: 10 (minimum 6). 106+ is an alternative Dynamic Kalman we are also testing. Once we have determined which is the most appropriate for the majority of users, we will be simplifying this option.
* IMUF 1.0.5 fixes an issue with crc checking within IMUF.
* BuF 3.5.1 requires IMUF 1.0.5 and fixes an issue where gyro calibration did not always occur correctly.
* BuF 3.5.1 release notes: https://github.com/ButterFlight/butterflight/releases/tag/3.5.1-RC1
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
* Known issue: When switching to Dshot1200 & 32k pid loop if the CPU is at 75%, reboot the FC because the auto-overclock to 216MHZ did not take effect.

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
