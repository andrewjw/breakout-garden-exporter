# CHANGELOG

<!-- version list -->

## v2.2.0 (2026-01-16)

### Chores

- Add support for Python 3.13 and drop Python 3.8.
  ([#71](https://github.com/andrewjw/breakout-garden-exporter/pull/71),
  [`6d86725`](https://github.com/andrewjw/breakout-garden-exporter/commit/6d8672504271e7000f62633d5a76c87d4b9c6f3e))

- Switch to using Coveralls github action for submitting coverage.
  ([#71](https://github.com/andrewjw/breakout-garden-exporter/pull/71),
  [`6d86725`](https://github.com/andrewjw/breakout-garden-exporter/commit/6d8672504271e7000f62633d5a76c87d4b9c6f3e))

### Features

- Add support for PM2.5 air quality sensors.
  ([#71](https://github.com/andrewjw/breakout-garden-exporter/pull/71),
  [`6d86725`](https://github.com/andrewjw/breakout-garden-exporter/commit/6d8672504271e7000f62633d5a76c87d4b9c6f3e))

- Drop support for Python 3.9 and add 3.14.
  ([`b1bf35b`](https://github.com/andrewjw/breakout-garden-exporter/commit/b1bf35bdc9b3897f114fb539dacbf70fa7b46144))


## v2.1.2 (2025-06-26)

### Bug Fixes

- Start periodic measurements for the SCD4X.
  ([`244f553`](https://github.com/andrewjw/breakout-garden-exporter/commit/244f5530f05c4b09b20f02ced27bb5f9e9ca65d3))


## v2.1.1 (2025-06-26)

### Bug Fixes

- Handle data not ready from SCD4X.
  ([`56ba73d`](https://github.com/andrewjw/breakout-garden-exporter/commit/56ba73d1a2883821e2c59d1ef2ee1cb89f80db95))


## v2.1.0 (2025-06-26)

### Bug Fixes

- Fix handling of SCD4X self test function.
  ([`5da3fdd`](https://github.com/andrewjw/breakout-garden-exporter/commit/5da3fdd59e9d957e6639f1494ca65640f3fd2e2b))

### Chores

- Add stubs for SCD4X library.
  ([`4265545`](https://github.com/andrewjw/breakout-garden-exporter/commit/4265545584263657037cc902ed93dcbcf3b0f9f5))

### Features

- Add support for the SCD4x CO2, temperature and humidity sensor.
  ([`8370bd4`](https://github.com/andrewjw/breakout-garden-exporter/commit/8370bd40aa2152c163d6b0e47093149b6203fb80))


## v2.0.0 (2025-05-29)

### Features

- Remove support for Python 3.8.
  ([`218883d`](https://github.com/andrewjw/breakout-garden-exporter/commit/218883dfaf019af059676f5c7a15946b471adbe3))

### Breaking Changes

- Removed support for Python 3.8.


## v1.0.0 (2025-05-29)

### Chores

- Update readme
  ([`a92d9ae`](https://github.com/andrewjw/breakout-garden-exporter/commit/a92d9aea218d15cc9e54e51fbefaeaa6cff63412))


## v0.6.0 (2025-01-12)

### Bug Fixes

- Remove debug code.
  ([`b6b7564`](https://github.com/andrewjw/breakout-garden-exporter/commit/b6b7564b4373ed982ef479e4d63b8a4248eb9131))

### Chores

- Fix PM25 tests ([#85](https://github.com/andrewjw/breakout-garden-exporter/pull/85),
  [`eabe26b`](https://github.com/andrewjw/breakout-garden-exporter/commit/eabe26b037af37e7f22bfd03daab3d205f793121))

- Set executable flag.
  ([`e33e52c`](https://github.com/andrewjw/breakout-garden-exporter/commit/e33e52c12fc91a97f567d57efa59b8d093be9636))

### Features

- Add support for PM2.5 air quality sensors.
  ([`aca44a8`](https://github.com/andrewjw/breakout-garden-exporter/commit/aca44a83dd63c77d2927f4168ffadc6bd7c97a93))


## v0.5.0 (2023-11-22)

### Bug Fixes

- Fix tests on Python 3.12.
  ([`076631e`](https://github.com/andrewjw/breakout-garden-exporter/commit/076631ecdd0826f449514369ae5fc773ed6c104f))

### Chores

- Add download stats badge to readme.
  ([`08c0027`](https://github.com/andrewjw/breakout-garden-exporter/commit/08c00279ef71785efe98c4993f95295085a3c4f1))

- Add link to PyPI
  ([`cc8cce6`](https://github.com/andrewjw/breakout-garden-exporter/commit/cc8cce62566bacdc68ef8d0a3feb09ee23f20ffd))

- Fix typo.
  ([`3def9fe`](https://github.com/andrewjw/breakout-garden-exporter/commit/3def9fe4a1f1a3f1d6b2b476ac8cbfb706580475))

### Features

- Add support for Python 3.12.
  ([`538245b`](https://github.com/andrewjw/breakout-garden-exporter/commit/538245b4ad8116744b38548f83429012f784cdef))


## v0.4.6 (2023-08-27)

### Bug Fixes

- Fix releases with semantic-release v8.
  ([`afa307f`](https://github.com/andrewjw/breakout-garden-exporter/commit/afa307fdc323cda325ff5dc0ba5a3f2294588980))


## v0.4.5 (2023-07-31)

### Bug Fixes

- Correct GitHub token
  ([`42b14ed`](https://github.com/andrewjw/breakout-garden-exporter/commit/42b14edab609ab8402087fcd5b8ffee1c80b5c38))


## v0.4.4 (2023-07-31)

### Bug Fixes

- Typo in semantic-release config.
  ([`f834033`](https://github.com/andrewjw/breakout-garden-exporter/commit/f8340333e9c81e7e4fdaf9ef66c12e51f4b3de91))


## v0.4.3 (2023-07-31)

### Bug Fixes

- Tell semantic-release to update the version variable.
  ([`faedd07`](https://github.com/andrewjw/breakout-garden-exporter/commit/faedd07902e328143fda17d51820a7b11cc0e36e))


## v0.4.2 (2023-07-31)

### Bug Fixes

- Pass config to semantic-release
  ([`86be6cd`](https://github.com/andrewjw/breakout-garden-exporter/commit/86be6cd4ac7f851fd87871d4a2fff92eda413b68))

### Chores

- Allow wheels to be built.
  ([`19c56d1`](https://github.com/andrewjw/breakout-garden-exporter/commit/19c56d1d49743df16ae40c5f48e4a57abd163c27))


## v0.4.1 (2023-07-31)

### Bug Fixes

- Run build commands to produce artifacts
  ([`7675f2a`](https://github.com/andrewjw/breakout-garden-exporter/commit/7675f2a39f74895d9fd38c63c83e4dc6d9ec65ae))


## v0.4.0 (2023-07-31)

### Chores

- Fix workflow to use semantic-release v8 command
  ([`e5b6d44`](https://github.com/andrewjw/breakout-garden-exporter/commit/e5b6d44b007303113ea69e9c8803aa256a6ce079))

- Trying to fix semanic-release v8 changes
  ([`e2d364c`](https://github.com/andrewjw/breakout-garden-exporter/commit/e2d364c37e6a2bdf4cf1f761d48936bfda789bc6))

- Trying to fix semanic-release v8 changes
  ([`a95c372`](https://github.com/andrewjw/breakout-garden-exporter/commit/a95c372b2afe121fa2ae71d5bcfa31318275183b))


## v0.3.1 (2023-07-16)

### Bug Fixes

- Fix code style.
  ([`bbe3944`](https://github.com/andrewjw/breakout-garden-exporter/commit/bbe394497367f0de2254b9a602bff7552be89518))

- Fix tests.
  ([`36478d5`](https://github.com/andrewjw/breakout-garden-exporter/commit/36478d54b4f36588a8f4db79b6e6288c245490b7))

- Handle a missing SGP30.
  ([`543d9af`](https://github.com/andrewjw/breakout-garden-exporter/commit/543d9af4942e1fe083eeb6cbf086863573026b9a))

- Handle an error when no i2c interface is found.
  ([`27c4776`](https://github.com/andrewjw/breakout-garden-exporter/commit/27c4776ca1fbe375d4000fcdd3138ac0452f9438))

- Handle missing BME280 sensor.
  ([`371f314`](https://github.com/andrewjw/breakout-garden-exporter/commit/371f314d2f4e88e57778bdbf38962f2879e11cb7))

- Handle missing ICP10125 sensor.
  ([`c7a2ed2`](https://github.com/andrewjw/breakout-garden-exporter/commit/c7a2ed28c4a7f29f92b625a3b411d96c0ff529eb))

### Features

- Add support for BME280.
  ([`508b8b2`](https://github.com/andrewjw/breakout-garden-exporter/commit/508b8b269c0185e1eba0bbae2dcb076bbc6cc0f7))


## v0.3.0 (2023-07-13)

### Chores

- Fix publish to PyPI
  ([`d287b3b`](https://github.com/andrewjw/breakout-garden-exporter/commit/d287b3bdb4e7581131cdbd7b627da98301693ae6))

- Fix typing and style errors.
  ([`0fab9af`](https://github.com/andrewjw/breakout-garden-exporter/commit/0fab9af422f477549e3610b54c2edcbaae292fd9))

- Improve test coverage.
  ([`07e65fd`](https://github.com/andrewjw/breakout-garden-exporter/commit/07e65fd1d9a32e01f6302f4d73892e19ce88030f))

### Features

- Add support for the SGP30 air quality sensor.
  ([`2b8584f`](https://github.com/andrewjw/breakout-garden-exporter/commit/2b8584f5b2bbffbeba6e00f957c0cca8af5b1866))


## v0.2.0 (2023-07-08)

### Chores

- Fix copy and paste error.
  ([`9039f6e`](https://github.com/andrewjw/breakout-garden-exporter/commit/9039f6e3056e64bfbc10908a16e0a7f140d9e1fa))

### Features

- Add command line options to readme.
  ([`01771cd`](https://github.com/andrewjw/breakout-garden-exporter/commit/01771cd9f7f5f24c76788f02d06253ea5cdc48f9))


## v0.1.0 (2023-07-08)

- Initial Release
