from gym.envs.registration import register

register(
    id='SoloEscape-v0',
    entry_point='gym_roundrobot.envs:SoloEscapeEnv',
)
