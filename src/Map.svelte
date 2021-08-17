<script>
	import { onMount, setContext } from 'svelte';
	import { mapbox, MapboxDraw, key } from './mapbox.js';


	setContext(key, {
		getMap: () => map
	});

	export let lat;
	export let lon;
	export let zoom;

	let container;
	let map;

	onMount(() => {
		const link = document.createElement('link');
		link.rel = 'stylesheet';
		link.href = 'https://unpkg.com/mapbox-gl/dist/mapbox-gl.css';

		link.onload = () => {
			map = new mapbox.Map({
				container,
				style: 'mapbox://styles/mapbox/satellite-v9',
				center: [lon, lat],
				zoom
			});

			// Drawing of polygon on map
			var draw = new MapboxDraw({
				displayControlsDefault: false,
				controls: {
					polygon: true,
					trash: true,
				},
			});

			// +/- buttons to zoom in and out
			var zoomButtons = new mapbox.NavigationControl({
				showCompass: false,
				visualizePitch: false,
			});

			map.addControl(draw, 'top-left');
			map.addControl(zoomButtons);

			map.on('draw.create', getMidPoint);
			map.on('draw.delete', getMidPoint);
			map.on('draw.update', getMidPoint);
			// When the polygon is complete the bounding box can be used to query OSM
			function getMidPoint(e) {
				const data = draw.getAll();
				const edgeNodes = data['features'][0]['geometry']['coordinates'][0];
				console.log(edgeNodes);
			}
		};

		document.head.appendChild(link);
		
		return () => {
			map.remove();
			link.parentNode.removeChild(link);
		};
	});
</script>

<div bind:this={container}>
	{#if map}
		<slot></slot>
	{/if}
</div>

<style>
	div {
		width: 100%;
		height: 80%;
		border-radius: 10px;
	}
</style>