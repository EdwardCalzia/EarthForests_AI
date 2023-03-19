import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig = plt.figure()

# Create a new basemap instance
m = Basemap(projection='merc', llcrnrlon=-180, llcrnrlat=-80, urcrnrlon=180, urcrnrlat=80, resolution='c')

m.drawcoastlines()
m.drawcountries()
m.drawstates()

# Add a satellite image of the earth with forest cover using the bluemarble() method
m.bluemarble()

plt.title('Satellite Image of the Earth with Forest Cover')
plt.show()
