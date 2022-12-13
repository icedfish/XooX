function FindProxyForURL(_url_, host) {

    var pos, exits = ["DIRECT", "SOCKS5 pac.yubing.work:7891; PROXY pac.yubing.work:7890;"];

    //0 for Direct，1 for Proxy
    var list = {
       "360buyimg.com":0, "adservice.google.com":1, "advanceautoparts.com":1, "akamaihd.net":1, "akamaized.net":1, "alicdn.com":0, "alipay.com":0, "apache.org":1,"android.com":1, "apple.com":0, "archive.org":1, "aspnetcdn.com":1, "atlassian.com":1, "autozone.com":1, "asco.org":1, "baidu.com":0, "bbc.co.uk":1, "bbc.com":1, "bbci.co.uk":1, "bdstatic.com":0, "bit.ly":1, "blogspot.com":1, "blogspot.hk":1, "box.com":1, "box.net":1, "boxcdn.net":1, "careforcar.co.th":1, "cdn.sstatic.net":1, "clients3.google.com":0,"cancer.gov":1, "cloudflare.com":1, "cloudfront.net":1,  "connect.8x8.com":1, "discord.com":1, "discordapp.com":1, "deepl.com":1, "esmo.org":1, "facebook.com":1,"facebook.net":1, "fbcdn.net":1, "fbsbx.com":1, "figma.com":1, "finance.yahoo.com":1, "ggpht.com":1, "gitbook.com":1, "github.com":1, "github.io":1, "githubassets.com":1, "githubusercontent.com":1, "gitlab-static.net":1, "gitlab.com":1, "golang.org":1, "goo.gl":1, "google":1, "google.com":1,"withgoogle.com":1, "google.com.hk":1, "googleapis.com":1, "googletagmanager.com":1, "googleusercontent.com":1, "googlevideo.com":1, "gstatic.com":1, "gtimg.com":0, "hkexnews.hk":1,"instagram.com":1,  "iqiyi.com":0, "jd.com":0, "jenkins.io":1, "jfrog.com":1, "jsdelivr.net":1, "khanacademy.org":1,"kastatic.org":1,"lcdn.com":1, "line.biz":1, "line.me":1, "licdn.com":1, "linkedin.com":1, "live.com":1,  "medium.com":1,"meta.com":1, "mtalk.google.com":0, "nih.gov":1, "notion.so":1,"nssurge.com":1, "onenote.com":1, "onenote.net":1, "openvpn.net":1, "openvpn.org":1, "pubmed.org":1, "pmthinking.com":1, "qq.com":0, "qlogo.cn":0, "myqcloud.com":0, "quora.com":1, "quoracdn.net":1, "redis.io":1, "reddit.com":1,"redd.it":1, "redditstatic.com":1,"redditmedia.com":1, "reuters.com":1, "s3.amazonaws.com":1, "safebrowsing.googleapis.com":0,  "sdk.split.io":1, "sec.report":1, "slideshare.net":1, "stackoverflow.com":1,  "times.com":1, "t.co":1, "t.me":1, "taobao.com":0, "telegram.org":1, "tensorflow.org":1, "tiktok.com":1, "tiktokcdn.com":1, "trellocdn.com":1, "twimg.com":1, "twitter.com":1, "v2ex.com":1, "videoscribe.co":1, "vimeo.com":1, "wikimedia.org":1, "wikipedia.org":1, "wireguard.com":1, "wsj.com":1, "yahoo.com":1, "yahoo.com.tw":1, "yimg.com":1, "ykimg.com":0, "youku.com":0, "youtu.be":1, "youtube.com":1, "ytimg.com":1, "zoom.us":1, "1password.com":1
    };
    do {
        if (list.hasOwnProperty(host)) return exits[list[host]];
        pos = host.indexOf(".") + 1;
        host = host.slice(pos)
    } while (pos >= 1)

    return "DIRECT";
}