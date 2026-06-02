import geopandas as gpd

f0 = 'active_area.shp'
f1 = "inactive_area.shp"


gdfa = gpd.read_file(f0)
gdfi = gpd.read_file(f1)


gdfx = gdfa.overlay(gdfi, how='symmetric_difference')
gdfx.to_file("model_boundary.shp")
