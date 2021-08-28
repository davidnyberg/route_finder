import mapbox from 'mapbox-gl';
import MapboxDraw from "@mapbox/mapbox-gl-draw";
import '@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw.css';

mapbox.accessToken = process.env.MAPBOXKEY;

const key = {};

export { mapbox, MapboxDraw, key };