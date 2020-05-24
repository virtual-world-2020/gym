import gym

env = gym.make("Taxi-v3") #创建出租车游戏环境
state = env.reset() #初始化环境
# 随机动作
conter = 0
reward = None
env.render()
print(env.action_space.sample)
print(env.observation_space)
R_cum = 0  # 累计reward
while reward!=20:
    state, reward, done, info = env.step(env.action_space.sample())
    conter = conter +1
    env.render()
    R_cum=R_cum+reward
print("counter ==",conter)
print("R_cum ==",R_cum)
