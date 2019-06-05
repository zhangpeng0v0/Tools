# 解析带有冒号的字符串
def analysisByColon(s):
    '''
    :param s: 是一个多行字符串
    :return: 返回一个格式化之后的字典
    '''
    temp={}
    dataList=s.split('\n')
    for i in dataList:
        if i=='' or i.isspace():
            continue
        else:
            dataList2=i.split(':')
            if len(dataList2) <= 1:
                try:
                    temp[dataList2[0].strip()]
                except:
                    pass
                temp[dataList2[0].strip()] = ''
            else:
                temp[dataList2[0].strip()]=dataList2[1].strip()
    return temp

# 解析带有等号的字符串
def analysisByEqual(s):
    temp = {}
    dataList = s.split(';')
    for i in dataList:
        if i == '' or i.isspace():
            continue
        else:
            dataList2 = i.split('=')
            if len(dataList2)<=1:
                temp[dataList2[0].strip()]=''
            temp[dataList2[0].strip()] = dataList2[1].strip()
    return temp

if __name__ == '__main__':

    s='adfbid2=0; sts_deviceid=16855a20d8443d-0786d15818d698-5d1f3b1c-1044480-16855a20d85754; _jzqx=1.1547624940.1547624940.1.jzqsr=ts%2Ezhaopin%2Ecom|jzqct=/jump/index_new%2Ehtml.-; JSloginnamecookie=18730231911; JSShowname=%E8%B5%B5%E9%B9%8F%E9%A3%9E; acw_tc=3ccdc15615476251554815562e40e8fa12b6d5706eddd068b897f6cbc08e83; adfbid=0; ZP_OLD_FLAG=false; dywea=95841923.1897540460572125700.1547624907.1547624907.1548057832.2; dywec=95841923; dywez=95841923.1548057832.2.2.dywecsr=baidupcpz|dyweccn=(not%20set)|dywecmd=cpt|dywectr=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1547624961,1548057833; sts_sg=1; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C05x-60KqiAsarxRNT00000Ftg0dC000000ToeAW.THLyktAJdIjA80K85Hb1nHR1PHRLgv99UdqsusK15yPBPyRkuHF-nj0snj0LPW60IHdjnYPAPbmznHm1nWRLnYw7PWujf1nknH0dwj7APjTzPfK95gTqFhdWpyfqn1DLn1TvP1bznBusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA7ETA-8QhPEUHq1pyfqnHcknHD1rj01FMNYUNq1ULNzmvRqmh7GuZNsmLKlFMNYUNqVuywGIyYqmLKY0APzm1Yzn163P0%26tpl%3Dtpl_11535_18778_14772%26l%3D1510152095%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3173767922_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D147%26ie%3Dutf-8%26f%3D8%26tn%3D93153557_hao_pg%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26oq%3Dgoogle%26rqlang%3Dcn%26inputT%3D6085; __utma=269921210.1814771033.1547624911.1547624911.1548057834.2; __utmc=269921210; __utmz=269921210.1548057834.2.2.utmcsr=baidupcpz|utmccn=(not%20set)|utmcmd=cpt|utmctr=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; _jzqa=1.1153422773997826000.1547624940.1547624940.1548057849.2; _jzqc=1; _jzqy=1.1548057849.1548057849.1.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98.-; _jzqckmp=1; __xsptplus30=30.2.1548057938.1548057938.1%232%7Csp0.baidu.com%7C%7C%7C%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%7C%23%23M_bnfRlfv4UItRESaAFToA_I9zK8C6kM%23; firstchannelurl=https%3A//passport.zhaopin.com/login; lastchannelurl=https%3A//ts.zhaopin.com/jump/index_new.html%3Futm_source%3Dbaidupcpz%26utm_medium%3Dcpt%26utm_provider%3Dpartner%26sid%3D121113803%26site%3Dnull; JsNewlogin=1905747548; at=f2f97395d99141e7a909650a3f557d1b; Token=f2f97395d99141e7a909650a3f557d1b; rt=2688f876314d4afa8e70a7cc2a1baa46; JSpUserInfo=3e692f645b6a5f64406b5c6b56665e695d735a695364546a52643f6b276b59665b695c735c695864566a5b64406b586b5d665b69557350693e64286a546406e626f5bafe5169217326695664576a58644b6b5b6b526653695c735d695a64526a2964026b186b4a6609690b7306695064356a3d644e6b586b5f662b69307356695b644b6a5864536b586b5266506955735b695064276a25644e6b586b5f663f692573566921642b6a5a64466b5b6b506653695573536959645f6a5264266b3d6b59665b695f73386922645b6a5964486b4; uiioit=377220665963526656675166576456725d6655635c6657675f6627642672596654635f660; jobRiskWarning=true; loginreleased=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22635249182%22%2C%22%24device_id%22%3A%2216855a1ffee7a6-030b7ae9fefb92-5d1f3b1c-1044480-16855a1fff035a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%2216855a1ffee7a6-030b7ae9fefb92-5d1f3b1c-1044480-16855a1fff035a%22%7D; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; LastCity=%E5%8C%97%E4%BA%AC; LastCity%5Fid=530; sts_sid=1686fd00fac40-001f327a3159f5-5d1f3b1c-1044480-1686fd00fadcf2; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22e91c48e8-170e-4f84-bbb4-671ebba67430-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22//jobs%22:{%22actionid%22:%227d3f49d2-4e67-4a79-81e3-dd739630480c-jobs%22%2C%22funczone%22:%22dtl_best_for_you%22}}; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1548064135; sts_evtseq=3'
    print(analysisByEqual(s))









