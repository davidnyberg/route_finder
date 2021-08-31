import mapbox from 'mapbox-gl';
import MapboxDraw from "@mapbox/mapbox-gl-draw";
import '@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw.css';


//weird hack to fix env vars...
const env_var = __myapp
const sub_env_var = env_var.env
mapbox.accessToken = sub_env_var.MAPBOXKEY;

const key = {};

export { mapbox, MapboxDraw, key };