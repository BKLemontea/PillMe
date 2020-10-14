mobiscroll.settings = {
    theme: 'ios',
    themeVariant: 'light'
};

$(function () {

    var timeValue = ["오전", "오후"],
        hourValue = [],
        minValues = [];

    for (var i = 1; i <= 12; i += 1) {
        hourValue.push({
            display: i,
            value: i,
        });
    }

    for (var i = 0; i < 60; i += 1) {
        minValues.push({
            display: i,
            value: i,
        });
    }


    $('#demo-mobile').mobiscroll().scroller({
        display: 'inline',
        width: 70,
        wheels: [
            [{
                circular: false,
                data: timeValue,
                label: ''
            }, {
                circular: false,
                data: hourValue,
                label: '시'
            }, {
                circular: false,
                data: minValues,
                label: '분'
            }]
        ],
        showLabel: true,
    });
});