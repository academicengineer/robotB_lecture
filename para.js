$(function(){
    var qis, ip, als = {};
    // ポーズボタンclickイベント
    $('#para-btn').on('click', function(){
        // 入力IP取得
        ip = $('#ip').val();
        // NAOqi Session 生成
        qis = new QiSession(ip);
        // 接続
        qis.socket()
        .on('connect', function(){
            // 接続成功
            console.log('[CONNECTED]');

            // ALTextToSpeechを使う
            qis.service('ALMotion').done(function(alm){
                als.ALMotion = alm;
                //console.log('接続成功');
                alm.setAngles(["HeadYaw", "HeadPitch"], [2.0, 0.0], 0.1);
            });

            // 接続断
            //console.log('[DISCONNECTED]');
        })
        
        .on('error', function(){
            // 接続エラー
            console.log('[CONNECTION ERROR]');
            qis.service('ALAnimatedSpeech').done(function(aas){
                als.alAnimatedSpeech = aas;
                aas.say('NAO、起動に失敗しました');
            });
        });
    });
});
