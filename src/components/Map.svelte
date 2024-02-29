<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';

    const yasmarina = `${base}/abu-dhabi.avif`;

    function updateZoomLevel() {
        const screenWidth = window.innerWidth;
        zoomLevel = screenWidth <= 600 ? 4 : 5.85; // adjust values as needed
    }

    function handleResize() {
        updateZoomLevel();
        map.setZoom(zoomLevel);
    }

    onMount(() => {
        updateZoomLevel();
        const svg = d3.select('#d3-container');
        const width = +svg.style('width').replace('px', '');
        const height = +svg.style('height').replace('px', '');
        
        svg.append('image')
           .attr('xlink:href', yasmarina)
           .attr('width', width)
           .attr('height', height)
           .attr('prserveAspectRatio', 'xMidYMid meet')
    });
</script>

<svg id='d3-container'></svg>
<style>
    #d3-container {
        width: 100%;
        height: 100%;
        background-color: #f0f0f0;
    }
</style>