(function() {
    $("#birthday").datepicker({
        changeMonth: true,
        changeYear: true,
        defaultDate: new Date(1990,1,1),
        maxDate: 0
    });
    $("#onboard").datepicker({
        changeMonth: true,
        changeYear: true,
        minDate: '01/01/1993',
        maxDate: 0
    });
})();
