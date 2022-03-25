from classes.DQL import DQL
from classes.Model import *
import gym
import torch
from Utilities import argmax

evaluate = False

env = gym.make('CartPole-v1')
# net = NN(4, 2, 1, 8)
net = MLP(4, 2)
# loss = torch.nn.SmoothL1Loss()
# loss = torch.nn.L1Loss()
loss = torch.nn.MSELoss()
# optimizer = torch.optim.SGD(net.parameters(), lr=1e-3)
# optimizer = torch.optim.Adam(net.parameters(), lr=1e-3)
optimizer = torch.optim.RMSprop(net.parameters(), lr=1e-3)
dql = DQL(
    rb_size=10000, batch_size=2, n_episodes=6000, device="cpu",
    loss=loss, optimizer=optimizer, gamma=0.99,
    policy="egreedy", epsilon=(0.01, 0.99, 1000), temp=0.1,
    model=net, target_model=True, tm_wait=20, env=env, render=False
)
dql()

if evaluate:
    done = False
    s = env.reset()
    while not done:
        env.render()
        s, _, _, done = env.step(int(argmax(net.forward(torch.tensor(s), "cpu"))))
    env.reset()