
Import("env")

print(env.Dump())

board_config = env.BoardConfig()
board_config.update("build.hwids", [
  ["0x4545", "0x4545"]
])