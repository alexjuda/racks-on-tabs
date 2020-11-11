(function () {
    function shouldFetchRows(interactionEntries) {
        console.assert(interactionEntries.length === 1);
        return interactionEntries[0].isIntersecting;
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
