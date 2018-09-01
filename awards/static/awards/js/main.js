$(document).ready(function() {
    $("#id_level").change(function() {
        var lvl = $("#id_level").val();

        $("#id_mee_score").removeAttr("required disabled");
        $("#id_mts_score").removeAttr("required disabled");
        $("#id_pds_score").removeAttr("required disabled");
        $("#id_gpa").removeAttr("required disabled")
        $("#id_pgpa").removeAttr("required disabled");
        $("#id_ccgpa").removeAttr("required disabled");
        $("#id_pcgpa").removeAttr("required disabled");

        if (lvl == "100") {
            $("#id_gpa").attr("required", "true");
            $("#id_mee_score").attr("required", "true");
            $("#id_mts_score").attr("required", "true");
            $("#id_pds_score").attr("disabled", "true");
            $("#id_pgpa").attr("disabled", "true");
            $("#id_ccgpa").attr("disabled", "true");
            $("#id_pcgpa").attr("disabled", "true");
        } else if (lvl == "200" || lvl == "300") {
            $("#id_gpa").attr("required", "true");
            $("#id_pgpa").attr("required", "true");
            $("#id_ccgpa").attr("required", "true");
            $("#id_pcgpa").attr("required", "true");
            $("#id_mee_score").attr("disabled", "true");
            $("#id_mts_score").attr("disabled", "true");
            $("#id_pds_score").attr("disabled", "true");
        } else {
            $("#id_pds_score").attr("required", "true");
            $("#id_gpa").attr("disabled", "true");
            $("#id_pgpa").attr("disabled", "true");
            $("#id_ccgpa").attr("disabled", "true");
            $("#id_pcgpa").attr("disabled", "true");
            $("#id_mee_score").attr("disabled", "true");
            $("#id_mts_score").attr("disabled", "true");
        }
    });

    $('#id_status').change(function() {
        var st = $("#id_status").val();

        $("#id_unit").removeAttr("disabled required");

        if (st == "Leader" || st == "Worker") {
            $("#id_unit").attr("required", "true");
        } else {
            $("#id_unit").attr("disabled", "true");
        }
    });

    $('#submitbtn').click(function() {
        $('#idModal').click();
    });

    $('#printBtn').click(function() {
        print();
    });
});