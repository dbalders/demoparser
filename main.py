from demoparser2 import DemoParser

wanted_props = ["m_vecX", "m_vecY"]
parser = DemoParser("/home/laiho/Documents/demos/cs2/s2.dem")
df = parser.parse_ticks(wanted_props, ticks=[x for x in range(29000, 30000)])
print(df)