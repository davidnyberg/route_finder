<script>
	import Map from './Map.svelte';
	//import MapMarker from './MapMarker.svelte';
	
	let showMap = {visible: false};

	function handleShowMap() {
		showMap.visible = !showMap.visible
	}

	function findTrailsOSM() {
		console.log("OSM");
		fetch("/get_trails?coordinates=test")
	}
</script>


<p>Find your next walk/run/bike route!</p>

<div>
{#if showMap.visible}
	<button on:click={handleShowMap}>
		Hide map
	</button>
{:else}
	<button on:click={handleShowMap}>
		Show map
	</button>
{/if}

<button on:click={findTrailsOSM}>
	Find Trails
</button>
</div>

{#if showMap.visible}
	<!-- TODO: make markers dynamic from a query from osm -->
	<Map lat={59.3} lon={18} zoom={10}>
<!-- 		<MapMarker lat={37.8225} lon={-122.0024} label="Svelte Body Shaping"/>
		<MapMarker lat={33.8981} lon={-118.4169} label="Svelte Barbershop & Essentials"/>
		<MapMarker lat={29.7230} lon={-95.4189} label="Svelte Waxing Studio"/>
		<MapMarker lat={28.3378} lon={-81.3966} label="Svelte 30 Nutritional Consultants"/>
		<MapMarker lat={40.6483} lon={-74.0237} label="Svelte Brands LLC"/>
		<MapMarker lat={40.6986} lon={-74.4100} label="Svelte Medical Systems"/> -->
	</Map>
{:else}
{/if}

<style>
	p {
		font-family: monospace;
		font-size: 3em;
		text-align: center;
	}

	div {
		text-align: center;
	}

	button {
		border-radius: 10px;
	}
</style>