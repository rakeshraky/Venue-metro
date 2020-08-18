
<template>
    <b-card class="title card_animation" :title="member.firstname+' '+member.lastname" header-tag="header" footer-tag="footer">
    <template v-slot:header>
        <h6 vclass="mb-0" :class="[ (member.membership_status === 'ACTIVE') ? 'greenfont' : (member.membership_status === 'REUSED')? 'yellowfont':'redfont']">
            <mark :class="[ (member.membership_status === 'ACTIVE') ? 'greenmark' : (member.membership_status === 'REUSED')? 'yellowmark':'redmark']"></mark>
            {{member.membership_status}}</h6>
    </template>
    <b-card-text class="tag">{{member.tiergamingcategory}}</b-card-text>
    <div style="font-size:1vw;">
        <div class="row">
            <div class="col-xl-6 col-md-6 text-left">
            <label class="labels">Post:<span class="values">{{member.postal_code}}</span></label>
            <label class="labels">DOB:<span class="values">{{member.dob}}</span></label>
            </div>
            <div class="col-xl-6 col-md-6 text-right">
            <label class="labels">Account.No:<span class="values">{{member.accountid}}</span></label>
            <label class="labels">Exp:<span class="values">{{member.expirydate}}</span></label>
            </div>
        </div>
    </div>
    <template v-slot:footer>
    <div>
       <span class="right-icons" style="float:right;">
        <a href="javascript:void(0);" onclick="" data-tooltip="Associated Devices"><i class="fa fa-tablet" aria-hidden="true"></i></a>
        <a href="javascript:void(0);" onclick="" data-tooltip="Notes"><i class="fa fa-sticky-note" aria-hidden="true"></i></a>
        <a href="javascript:void(0);" onclick="" data-tooltip="Card Details"><i class="fa fa-credit-card" aria-hidden="true"></i></a>
        <a href="javascript:void(0);" onclick="" data-tooltip="Communication Details"><i class="fa fa-envelope" aria-hidden="true"></i></a>
    </span>
    </div>
    </template>
    </b-card>
</template>

<script>
export default {
    props:["member"]
}
</script>
<style scoped>
     mark {
    padding: 5px;
    content: "";
    font-size: 0px;
    border-radius: 20px;
    position: relative;
    top: -5px;
    margin-right: 4px;
}

.tag{
    font-weight: 800;
    color: steelblue;
}
.greenfont{
    color: #19c4ac;;
}
.redfont{
    color: #ff4d4d;
}
.yellowfont{
    color: #e7e701
}
.greenmark{
    background-color: #19c4ac;;
}
.redmark{
    background-color: #ff4d4d;
}
.yellowmark{
    background-color: #e7e701
}
</style>



