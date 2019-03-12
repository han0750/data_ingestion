
## 09277 박한주 
# Name the components on this agent
agent1.sources = mySource
agent1.sinks = mySink
agent1.channels = myChannel

# Describe/configure the source
agent1.sources.mySource.type = netcat
agent1.sources.mySource.bind = localhost
agent1.sources.mySource.port = 44444

# Describe the sink
agent1.sinks.mySink.type = logger


# Use a channel which buffers events in memory
agent1.channels.myChannel.type = memory
agent1.channels.myChannel.capacity = 1000
agent1.channels.myChannel.transactionCapacity = 100

# Bind the source and sink to the channel
agent1.sources.mySource.channels = myChannel
agent1.sinks.mySink.channel = myChannel
