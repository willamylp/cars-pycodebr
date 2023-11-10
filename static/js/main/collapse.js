function CollapseExpand(btn, icon) {
    const btnCollapseExpand = document.querySelector(btn);
    const iconCollapseExpand = document.querySelector(icon);

    btnCollapseExpand.onclick  = function () {
        if(iconCollapseExpand.classList[2] == "dw-down-chevron") {
            iconCollapseExpand.classList.remove('dw-down-chevron');
            iconCollapseExpand.classList.add('dw-up-chevron');
        }
        else {
            iconCollapseExpand.classList.add('dw-down-chevron');
            iconCollapseExpand.classList.remove('dw-up-chevron');
        }
    }
}