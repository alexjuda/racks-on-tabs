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

    function fetchPartialRows(nRows, afterId) {
        return fetch(`/partial/rows?n_rows=${nRows}&after_id=${afterId}`, {})
            .then(resp => {
                return resp.text();
            });
    }

    function csvTableElement() {
        return document.querySelector('#csv-table');
    }

    function postTablePElement() {
        return document.querySelector('#post-table-p');
    }

    function appendHtml(element, htmlString) {
        element.insertAdjacentHTML('beforeend', htmlString);
    }

    function setTextContent(element, content) {
        element.textContent = content;
    }

    const csvRowBatchSize = 10;

    window.addEventListener('load', _evt => {
        const obs = new IntersectionObserver(entries => {
            if (shouldFetchRows(entries)) {
                const maxId = maxCurrentRowId();

                setTextContent(postTablePElement(), 'loading next rows...');

                fetchPartialRows(csvRowBatchSize, maxId)
                    .then(html => {
                        appendHtml(csvTableElement(), html);

                        setTextContent(postTablePElement(), '');
                    });
            }
        }, {});
        obs.observe(postTablePElement());
    });
})();
