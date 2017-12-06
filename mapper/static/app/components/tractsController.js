mapper.controller("tractsController",['$scope','$log','$http','leafletData',function($scope,$log,$http,leafletData){
    $log.log("Hello from tracts controller");

    //$scope.selectedCounty = null;
    $scope.rawTractsData=null;


    //init map layers...
    leafletData.getMap().then(function(map){
	tractsLayer = new L.FeatureGroup();
	tractsLayer.addTo(map);
    });
    
    
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
	    

	    
	    if (t.diesel_conc[0].total_conc<2.5){
		polygonOptions.color="red";
	    }
	    
	    if (t.diesel_conc[0].total_conc<2){
		polygonOptions.color="orange";
	    }
	    
	    if(t.diesel_conc[0].total_conc<0.5){
		polygonOptions.color="green";
	    }

	    
	    var polygon = L.polygon(latlngs, polygonOptions) ;//.addTo(tractsLayer);

	    polygon.addTo(tractsLayer);
	}
    };
    
    $scope.changeCounty = function(countyId){
	//clear layer...
	tractsLayer.clearLayers();
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
