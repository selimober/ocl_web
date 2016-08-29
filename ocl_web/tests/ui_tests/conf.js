exports.config = {
    framework: 'jasmine',
    seleniumAddress: 'http://localhost:9515',
    // seleniumAddress: 'http://localhost:4444/wd/hub',
    specs: ['./specs/organization_spec.js','./specs/user_source_spec.js','./specs/collections_spec.js'],
    capabilities: {
        'browserName': 'phantomjs'
        // 'browserName': 'chrome'
    },
    baseUrl: 'http://showcase.openconceptlab.org'
};
