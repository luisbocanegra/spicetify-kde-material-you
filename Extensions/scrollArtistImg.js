function waitForElement(els, func, timeout = 100) {
    if (timeout == 1) {
        timeout = 10
    }
    const queries = els.map(el => document.querySelector(el));
    if (queries.every(a => a)) {
        func(queries);
    } else if (timeout > 0) {
        setTimeout(waitForElement, 300, els, func, --timeout);
    }
}
const timer = (ms) => new Promise((res) => setTimeout(res, ms));


async function main() {
    // We need to wrap the loop into an async function for this to work
    // for (var i = 0; i < 10; i++) {
    while (true) {
        // let photo2 = document.getElementsByClassName('main-entityHeader-gradient')[0].getAttribute('background-image');
        // var img = $('.main-entityHeader-gradient').attr('background-image');
        // console.log(photo2)

        // var img = document.getElementsByClassName("main-entityHeader-gradient")[0];
        // style = img.currentStyle || window.getComputedStyle(img, false),
        // bi = style.backgroundImage.slice(4, -1).replace(/"/g, "");
        // console.log(bi);
        try {
            var img = document.getElementsByClassName('main-entityHeader-gradient')[0],
            url = img.style.backgroundImage;

            var newPos = document.getElementsByClassName('main-entityHeader-withBackgroundImage')[0]
            // newPos.style.backgroundImage=url;

            var newDiv = document.getElementsByClassName('aaadd')[0]

            if (newDiv == null || newDiv =="") {
                newPos.innerHTML += '<div class="aaadd"></div>'
                newDiv = document.getElementsByClassName('aaadd')[0]
            }
            var st = newDiv.style;
            st.setProperty('background-image',url)
            st.setProperty('width','100%')
            st.setProperty('height','100%')
            st.setProperty('position','absolute')
            // st.setProperty('top','0')
            st.setProperty('left','0')
            st.setProperty('right','0')
            // st.setProperty('bottom','0')
            st.setProperty('margin','auto')
            // st.setProperty('opacity','0.3')

            // st = newPos.style;
            // st.setProperty('background-image',url)
            // st.setProperty(' background-blend-mode','lighten')
            
            console.log(url);
        } catch (err) {
            console.log(err)
        }
        
        await timer(500);
        // if (i == 10) {
        //     i=0;
        // }
        // then the created Promise can be awaited
        //}
    }
}


waitForElement(["main"], (root) => {
    // let spiceEq = getComputedStyle(document.querySelector(":root")).getPropertyValue("--spice-equalizer");
    // let eqColor = getKeyByValue(colorPalette, spiceEq);
    // root[0].classList.add(`catppuccin-eq-${eqColor}`);
    console.log("scrollArtistImg.js Loaded");
    // const imgClass = document.querySelector('.main-entityHeader-gradient')
    // const options = {
    // attributes: true
    // }

    // function callback(mutationList, observer) {
    // mutationList.forEach(function(mutation) {
    //     if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
    //     // handle class change
    //     console.log("Changed!");
    //     }
    // })
    // }
    // console.log(imgClass);

    // const observer = new MutationObserver(callback)
    // observer.observe(btn, options)
});

waitForElement([".main-entityHeader-gradient"], (root) => {
    // let spiceEq = getComputedStyle(document.querySelector(":root")).getPropertyValue("--spice-equalizer");
    // let eqColor = getKeyByValue(colorPalette, spiceEq);
    // root[0].classList.add(`catppuccin-eq-${eqColor}`);
    console.log("scrollArtistImg.js -> found .main-entityHeader-gradient");
    // const imgClass = document.querySelector('.main-entityHeader-gradient')
    // const options = {
    // attributes: true
    // }

    // function callback(mutationList, observer) {
    // mutationList.forEach(function(mutation) {
    //     if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
    //     // handle class change
    //     console.log("Changed!");
    //     }
    // })
    // }
    // console.log(imgClass);
    main();

    // const observer = new MutationObserver(callback)
    // observer.observe(btn, options)
});

