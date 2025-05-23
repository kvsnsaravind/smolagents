# -*- coding: utf-8 -*-
"""smolagents

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C9Yv7Mk38_T2o-Gh2fD3t_9O0V_wGidC

First install the package.
"""

!pip install smolagents

"""Define your agent, give it the tools it needs and run it!"""

from huggingface_hub import notebook_login

notebook_login()

from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel

model = InferenceClientModel()
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")

agent.run("What is the capital of France?")

agent.run("What is the capital of INDIA?")

