import mapbox from 'mapbox-gl';
import MapboxDraw from "@mapbox/mapbox-gl-draw";
import '@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw.css';



//TODO: make accesstoken a dev env variable so its not pushed to git
mapbox.accessToken = "pk.eyJ1IjoiZGF2aWRueWJlcmciLCJhIjoiY2tyMmc1cTN5MGswejJvcng1d2owZnR0YyJ9.931rNR_4eqyfhufFGPRMjg";

const key = {};

export { mapbox, MapboxDraw, key };