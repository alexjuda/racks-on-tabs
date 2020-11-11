(function () {
    // app state
    window.racksOnTabs = {}

    function readAppState(key) {
        return window.racksOnTabs[key];
    }

    function writeAppState(key, value) {
        window.racksOnTabs[key] = value;
    }

    function shouldFetchRows(interactionEntries) {
        console.assert(interactionEntries.length === 1);
        return interactionEntries[0].isIntersecting;
    }

    function maxByFn(coll, fn) {
        let maxValSoFar = null;
        let maxElementSoFar = null;
        coll.forEach(element => {
            if (maxValSoFar === null || fn(element) > maxValSoFar) {
                maxValSoFar = fn(element);
                maxElementSoFar = element;
            }
        });
        return maxElementSoFar;
    }

    function maxCurrentRowId() {
        const rowIds = [...document.querySelectorAll('.csv-table-row')]
              .map(e => { return e.getAttribute('data-row-id')});
        const maxRowId = Math.max(...rowIds);
        return (isFinite(maxRowId) ? maxRowId : -1);
    }

    const csvRowBatchSize = 10;

    window.addEventListener('load', _evt => {
        const obs = new IntersectionObserver(entries => {
            console.log(entries);
            document.querySelector('#debug-p').textContent = (entries[0].isIntersecting ? "intersecting": "not intersecting");

            if (shouldFetchRows(entries)) {
                const maxId = maxCurrentRowId();
                fetch(`/partial/rows?n_rows=${csvRowBatchSize}&after_id=${maxId}`, {})
                    .then(resp => {
                        return resp.text();
                    })
                    .then(fetchedHtml => {
                        document.querySelector('#csv-table').insertAdjacentHTML('beforeend', fetchedHtml);
                    });
            }
        }, {});
        obs.observe(document.querySelector('#post-table-p'))
    });
})();
