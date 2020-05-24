import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    state, reward, done, info=env.step(env.action_space.sample()) # take a random action
    if done:#结束了就从头再来
        env.reset()
env.close()