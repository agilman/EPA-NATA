mapper.controller("tractsController",['$scope','$log','$http','leafletData',function($scope,$log,$http,leafletData){
    $log.log("Hello from tracts controller");

    //$scope.selectedCounty = null;
    $scope.rawTractsData=null;


    //init map layers...
    leafletData.getMap().then(function(map){
	tractsLayer = new L.FeatureGroup();
	tractsLayer.addTo(map);
    });

    //center map
    angular.extend($scope, {
	center: {
	    lat: 40.0,
	    lng: -96,
	    zoom: 4
	}});
    
    
    $scope.changeState = function(data){
	loadCounties(data);
    };

    function loadCounties(stateId){
	$http.get('/api/stateCounties/'+stateId).then(function(data){
	    $scope.counties = data.data;
	});	
    };

    function drawTracts(tracts){
	for(var i=0;i<tracts.length;i++){
	    var t = tracts[i];
	    
	    var points = t.polygon;
	    
	    var latlngs = [];

	    for(var p=0;p<points.length;p++){
		
		latlngs.push([parseFloat(points[p].lat),parseFloat(points[p].lng)]);
		
	    }

	    
	    var polygonOptions = { color:'black',
				   weight:2,
				   fillOpacity: 0.75}
	    

	    
	    if (t.diesel_conc[0].total_conc<3){
		polygonOptions.color="red";
	    }
	    
	    if (t.diesel_conc[0].total_conc<2){
		polygonOptions.color="orange";
	    }

	    if (t.diesel_conc[0].total_conc<1){
		polygonOptions.color="blue";
	    }
	    
	    if(t.diesel_conc[0].total_conc<0.5){
		polygonOptions.color="green";
	    }

	    var polygon = new L.polygon(latlngs, polygonOptions).on('click',$scope.tractClick) ;//.addTo(tractsLayer);
	    polygon.diesel_conc = t.diesel_conc[0].total_conc;
	    polygon.tractId  = t.geoid;
	    polygon.population = t.population;
	    
	    polygon.addTo(tractsLayer);
	}
    };

    $scope.tractClick= function(tract){
	$scope.tractId = tract.target.tractId;
	$scope.diesel_conc = tract.target.diesel_conc;
	$scope.population = tract.target.population;
    };
    
    $scope.changeCounty = function(countyId){
	//clear layer...
	tractsLayer.clearLayers();
	//clear tract info...
	$scope.tractId = null;
	$scope.diesel_conc = null;
	$scope.population = null;
	
	$http.get('/api/diesel/'+$scope.selectedState+'/'+countyId).then(function(data){
	    $scope.rawTractsData = data.data;

	    drawTracts(data.data);

	    //attempt to fit map;
	    var bounds = tractsLayer.getBounds();
	    
	    leafletData.getMap().then(function(map) {
		map.fitBounds(bounds);
	    });
	    
	});
    }
}]);
