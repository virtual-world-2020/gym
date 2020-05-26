# gym虚拟环境中了解强化学习
***

## Introduction to gym
* Gym是用于开发和比较强化学习算法的工具包。 它支持让agents学习行走，也能让agents学习玩诸如Pong或Pinball之类的游戏  
它是用于强化学习任务的开源接口，提供了一套易于使用的强化学习任务。
* Gym提供环境,我们自己编写算法，编写算法时可以使用现有的数值计算库（例如TensorFlow)编写。  
* 网址：[gym.openai.com](https://gym.openai.com/)  
* documentation：[gym.openai.com/docs](https://gym.openai.com/docs/) 

### Preparatory work
* 必须安装python和pycharm，git为可选项。本节课用到的所有的材料也都放进了超星云盘中，邀请码:dyqk1179
* python3.5+
网址：[https://www.python.org](https://www.python.org)  
* 安装时注意勾选Add Python 3.8 to PATH,默认是不勾选的。
* python编辑器pycharm   
网址：[https://www.jetbrains.com/pycharm/download/#section=windows](https://www.jetbrains.com/pycharm/download/#section=windows) 
* installation options 中注意 那四个框全都勾上。
* 版本控制工具git  
网址：https://git-scm.com/downloads   
* 注意选择你的电脑对应的版本，pycharm选择Community即可，同学们可以通过复旦邮箱使用Professional版本，同学们可以自行去探索     

### 从github中clone本项目
* git from version control  
当同时安装了python,git,和pycharm时，打开pycharm,点击git from version control 并填写本例地址：https://github.com/virtual-world-2020/gym  ,可以将项目clone 到本地。

* 如果选择不装git,也可以直接从github上clone本项目到本地，解压本项目为一个文件夹，右键该文件夹，选择open Folder as pycharm Edition Project
              
#### Installation of gym
* pip 是 Python 包管理工具，该工具提供了对Python 包的查找、下载、安装、卸载的功能。
* 在学习python的时候，用pip下载一些库，有时候非常的慢，简直达到了奔溃的边缘。因为默认pip是使用Python官方的源，但是由于国外官方源经常被墙，导致不可以用，我们可以使用国内的Python镜像源，从而解决Python安装不上库的烦恼。
* 所以我们常常切换pip镜像源
* 可参考：[python - pip换源，更换pip源到国内镜像](https://blog.csdn.net/xuezhangjun0121/article/details/81664260) ,或者直接去百度一下。
* 更换pip源后，Terminal输入如下命令：
```shell script
pip install gym
```
### hello world
见testGym.py
```python
import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    state, reward, done, info=env.step(env.action_space.sample()) # take a random action
    if done:#结束了就从头再来
        env.reset()
env.close()
```
* 这算是gym的hello world程序，程序中，我们创建了gym 中名为'CartPole-v0'的环境，这样的环境还有很多，同学们可以在官方文档中查阅，强烈建议有兴趣的同学去阅读官方文档自行探索，本文档仅作指导作用。
* 由于我们还没有编写自己的算法，环境中执行动作时采用了随机动作。

### gym 中的重要概念
* 参考：[https://gym.openai.com/docs/](https://gym.openai.com/docs/)  
* Environments   
hello world 示例中展示了'CartPole-v0' 这个环境,通过“env = gym.make('X')”,创建不同的环境。
* Observations  
如果不想采用随机动作，而是根据掌握的当前环境的信息采取决定，那就需要Observations,环境的step方法恰好返回了我们所需要的Observations,step返回四个值。这些是：  
    - observation（object）：特定于环境的对象，代表您对环境的观察。
    - reward（float）：上一动作获得的奖励。
    - done（boolean）：是否需要reset再次进入环境，即该回合是否该结束了。
    - info（dict）：对调试有用的诊断信息。
* Spaces  
每个环境都带有action_space和observation_space，它们描述了有效操作和观察的范围。

### 强化学习
* 参考：[https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/](https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/)  
* 强化学习是机器学习大家族中的一大类, 是让计算机实现从一开始什么都不懂, 脑袋里没有一点想法, 通过不断地尝试, 从错误中学习, 最后找到规律, 学会了达到目的的方法. 这就是一个完整的强化学习过程.   
实际中的强化学习例子有很多. 比如近期最有名的 Alpha go, 机器头一次在围棋场上战胜人类高手, 让计算机自己学着玩经典游戏 Atari, 这些都是让计算机在不断的尝试中更新自己的行为准则, 从而一步步学会如何下好围棋, 如何操控游戏得到高分.

### Q learning  
* 强化学习中较为基础的一种
* Q为动作效用函数（action-utility function），用于评价在特定状态下采取某个动作的优劣，可以理解为效用值。它是智能体的记忆。
* 简单的说，Q learning 就是建立一个Q表格，记录了环境中所有状态下采取所有动作能够获得收益的期望，根据Q值来选取能够获得最大收益的动作。刚开始时，这个表格是不准的，我们常常将Q表初始化为0。
* 有利于最终目标的动作会获得正reward，不利于最终目标的动作会获得负reward，  
* 接下来，我们的agent(智能体)在环境中根据Q表进行探索，每一步都会有reward，根据这reward，更新Q表。随着agent的探索，Q表越来越完善，agent的行为也越来越智能，回合内的总reward也越来越高。
* Q table 中，纵轴是state，横轴是action。
* 两个重要因素  
    * 学习率 learning rate（alpha）:它定义了一个旧的Q值将从新的Q值哪里学到的新Q占自身的多少比重。值为0意味着代理不会学到任何东西（旧信息是重要的），值为1意味着新发现的信息是唯一重要的信息。
    * 折扣因子discount factor（gamma），它定义了未来奖励的重要性。值为0意味着只考虑短期奖励，其中1的值更重视长期奖励。
* 更新公式： Q(state, action) +=alpha( R(state, action) + Gamma * Max[Q(next state, all actions)] - Q(state, action) )
* 即 New Q value = Current Q value + alpha * [Reward + discount_rate * (highest Q value between possible actions from the new state s’ ) — Current Q value ]
* 释义：R(state, action) + Gamma * Max[Q(next state, all actions)] 是采取action后，和reward和next state联系起来的实实在在的Q值,可以视为Q现实，Q(state, action)记录了未采取action时的值，是我们估计的,估计的时候并不知道reward和下一个状态,视为Q估计,两者之差为现实与估计的差距。新Q(state, action)=老Q(state, action) + alpha * 差距
* 参考：[莫烦python](https://www.python.org)  

### Taxi-v3
* gym 中的一个环境
* Document：[https://gym.openai.com/envs/Taxi-v3/](https://gym.openai.com/envs/Taxi-v3/) 
* Github：[https://github.com/openai/gym/blob/master/gym/envs/toy_text/taxi.py ](https://github.com/openai/gym/blob/master/gym/envs/toy_text/taxi.py )  
* Description:  
在Map中有四个指定的位置，分别是R(ed)、G(reen)、Y(ellow)和B(lue)。当一回合开始时，出租车在广场中一个随机位置出发，乘客在RGYB中的一个随机的位置。出租车开到乘客的位置，接乘客，运送乘客到目的地(RGYB中的另一个)，然后放下乘客。一旦乘客下车，这一回合就结束了
* Map
```shell script
MAP = [
    "+---------+",
    "|R: | : :G|",
    "| : | : : |",
    "| : : : : |",
    "| | : | : |",
    "|Y| : |B: |",
    "+---------+",
]
```
* 彩图及含义:   
      
|  颜色   | 含义  |
|  ----  | ----  |
| 蓝色  | 乘客 |
| 洋红色  | 目的地 |
| 黄色 | 空出租车 |
| 绿色  | 载客出租车 |  

![avatar](https://s1.ax1x.com/2020/05/24/tSjFP0.png)  

* Observations:  
有500个离散状态，因为有25个出租车位置，乘客的5个可能位置(包括乘客在出租车中的情况)，和4个目的地位置。
* Actions:任何时刻，出租车都有六种行为  
    - move south
    - move north
    - move east 
    - move west 
    - pickup passenger
    - dropoff passenger
* Rewards:  
每一次行动都有-1的奖励，而运送乘客成功到达目的地则有+20的额外奖励。出租车仅能在乘客的位置执行“pickup”,仅能在目的地执行“dropoff”,非法执行“pickup”和“dropoff”的行为将得到-10的奖励。

### 案例

#####  1. 随机状态下
* 运行 random_taxi.py
在此状态下，出租车也能将乘客送到目的地，但是花费了大量的时间，还有很多非法行为——不该“pickup” 和“dropoff” 时“pickup”,“dropoff”了

#####  2. 使用Q learning 训练后
* 运行 testTaxi-v3.py, 运行程序前需要安装numpy
* NumPy 是一个运行速度非常快的数学库，主要用于数组计算
* 安装numpy,Terminal输入如下命令：
```shell script
pip install numpy
```
* 程序中我们建立了一个 (状态空间的大小)*(动作空间大小) 的 Q table ,然后使用Q-learning 算法进行训练。  

|   |move south     | move north | move east   |move west   | pickup passenger  |dropoff passenger  | 
|  ----  | ----  |  ----  | ----  |----  | ----  |----  |
| state1    | 0     | 0     | 0   |0   | 0  |0   |
| state2    | 0     | 0     | 0   |0   | 0  |0   |
| state3    | 0     | 0     | 0   |0   | 0  |0   |
| .    | 0     | 0     | 0   |0   | 0  |0   |
| . | 0     | 0     | 0   |0   | 0  |0   |
| 一共500个state    | 0     | 0     | 0   |0   | 0  |0   |
| .    | 0     | 0     | 0   |0   | 0  |0   |
| .   | 0     | 0     | 0   |0   | 0  |0   |
| .    | 0     | 0     | 0   |0   | 0  |0   |
|     | 0     | 0     | 0   |0   | 0  |0   |
| state500    | 0     | 0     | 0   |0   | 0  |0   |


* 训练过程中，每50个回合输出一次 total reward ,可见total reward是逐渐减小的。最后的波动是因为，出租车已经完全知道该怎么走了，total reward 决定于 乘客的地点和目的地和出租车的位置。
* 取消训练过程中对env.render()注释可以看到训练过程。
* 在最后的测试环节中可见，我们的出租车已经学会接送乘客了。

### 展望
* 细心的同学会发现，random_taxi.py 中total reward 很快就收敛了，训练 2000个episode 简直浪费，有能力的同学试一下写个终止条件让训练提前结束。
* 在普通的Q-learning中，当状态和动作空间是离散且维数不高时可使用Q-Table储存每个状态动作对的Q值，而当状态和动作空间是高维连续时，使用Q-Table描述动作空间和状态空间十分困难。
* 所以在此处可以把Q-table更新转化为一函数拟合问题，通过拟合一个函数function来代替Q-table产生Q值，使得相近的状态得到相近的输出动作。因此我们可以想到深度神经网络对复杂特征的提取有很好效果，所以可以将DeepLearning与Q learning结合这就成为了DQN(Deep Q Network)。
* 感兴趣的同学，可以尝试学习DQN用于解决 CartPole-v0 环境中的问题。
 
   

