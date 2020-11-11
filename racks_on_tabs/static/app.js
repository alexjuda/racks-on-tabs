(function () {
    // app state
    window.racksOnTabs = {
    };

    function shouldFetchRows(interactionEntries) {
        console.assert(interactionEntries.length === 1);
        return interactionEntries[0].isIntersecting;
    }

    window.addEventListener('load', _evt => {
        const obs = new IntersectionObserver(entries => {
            console.log(entries);
            document.querySelector('#debug-p').textContent = (entries[0].isIntersecting ? "intersecting": "not intersecting");

            if (shouldFetchRows(entries)) {
                fetch('/partial/rows', {})
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
