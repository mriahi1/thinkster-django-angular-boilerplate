(function() {
    'use strict';

    angular
        .module('thinkster', [
            'thinkster.routes',
            'thinkster.config',
            'thinkster.authentication',
            'thinkster.layout'
        ]);

    angular
        .module('thinkster.config', []);

    angular
        .module('thinkster.routes', ['ngRoute']);

    angular
        .module('thinkster')
        .run(run);

    run.$inject = ['$http'];

    /**
     * @name run
     * @desc Update xsrf $http headers to align with Django's defaults
     */
    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }
})();
