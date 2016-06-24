from ddlite import *
import BiomarkerCandidateGenerator, DiseaseCandidateGenerator


def doEverything():
    parser = DocParser('AGR2_blood_biomarker.txt', ftreader=TextReader())
    sentences = parser.parseDocSentences()

    BM = BiomarkerCandidateGenerator.generateBiomarkerCandidates()
    DM = DiseaseCandidateGenerator.generateDiseaseCandidates()

    possiblePairs = Relations(sentences, BM, DM)
    feats = possiblePairs.extract_features()
    otherModel = DDLiteModel(possiblePairs, feats)
    keyWords = ["associate", "express", "marker", "biomarker", "elevated", "decreased",
                "correlation", "correlates", "found", "diagnose", "variant", "appear",
                "connect", "relate", "exhibit", "indicate", "signify","show", "demonstrate",
                "reveal", "suggest", "evidence", "elevation", "indication", "diagnosis",
                "variation", "modification", "suggestion" , "link", "derivation", "denote",
                "denotation", "demonstration", "magnification", "depression", "boost", "level",
                "advance", "augmentation", "lessening", "enhancement","expression", "buildup",
                "diminishing", "diminishment", "reduction", "drop", "dwindling", "lowering"]
    negationWords = ["not", "nor", "neither"]
    def presenceOfNot(m):
        for word in negationWords:
            if (word in m.post_window1('lemmas')) and (word in m.pre_window2('lemmas')):
                return True
        return False

    # 1
    def LF_distance(m):
        distance = abs(m.e2_idxs[0] - m.e1_idxs[0])
        if distance < 10:
            # print "RETURNING ONE"
            return 0
        else:
            return -1
    def LF_keyword(m):
        for word in keyWords:
            if (word in m.post_window1('lemmas')) and (word in m.pre_window2('lemmas')):
                if presenceOfNot(m):
                    return -1
                else:
                    return 1
            else:
                return 0

    # def LF_associate(m):
    #     if ('associate' in m.post_window1('lemmas')) and ('associate' in m.pre_window2('lemmas')):
    #         return 1
    #     else:
    #         return 0
    # # 3
    # def LF_express(m):
    #     return 1 if ('express' in m.post_window1('lemmas')) and ('express' in m.pre_window2('lemmas')) else 0
    # # 4
    # def LF_marker(m):
    #     return 1 if ('marker' in m.post_window1('lemmas') or 'biomarker' in m.post_window1('lemmas')) and (
    #     'marker' in m.post_window2('lemmas') or 'biomarker' in m.post_window2('lemmas')) else 0
    # # 5
    # def LF_elevated(m):
    #     return 1 if ('elevated' in m.post_window1('lemmas')) and ('elevated' in m.pre_window2('lemmas')) else 0
    # def LF_decreased(m):
    #     return 1 if ('decreased' in m.post_window1('lemmas')) and ('decreased' in m.pre_window2('lemmas')) else 0
    # # 6
    # def LF_correlation(m):
    #     return 1 if ('correlation' in m.pre_window1('lemmas')) else 0
    # # 7
    # def LF_correlate(m):
    #     return 1 if ('correlates' in m.post_window1('lemmas')) and ('found' in m.pre_window2('lemmas')) else 0
    # # 8
    # def LF_found(m):
    #     return 1 if ('found' in m.post_window1('lemmas')) and ('found' in m.pre_window2('lemmas')) else 0
    # 9 (-1 if biomarker is confused with a name of a person)
    def LF_People(m):
        return -1 if ('NNP' in m.mention1(attribute='poses')) else 0
    # #10
    # def LF_diagnosed(m):
    #     return 1 if('diagnose' in m.post_window1('lemmas')) else 0
    # #11
    # def LF_variant(m):
    #     return 1 if('variant of' in m.pre_window1('lemmas')) else 0
    # #12
    # def LF_appear(m):
    #     return 1 if ('appear' in m.post_window1('lemmas')) else 0
    # #13
    # def LF_connect(m):
    #     return 1 if ('connect' in m.post_window1('lemmas')) else 0
    # #14
    # def LF_relate(m):
    #     return 1 if ('relate' in m.post_window1('lemmas')) else 0
    # #15
    # def LF_exhibit(m):
    #     return 1 if ('exhibit' in m.post_window1('lemmas')) else 0
    # #16
    # def LF_indicate(m):
    #     return 1 if ('indicate' in m.post_window1('lemmas')) else 0
    # #17
    # def LF_signify(m):
    #     return 1 if ('signify' in m.post_window1('lemmas')) else 0
    # #18
    # def LF_show(m):
    #     return 1 if ('show' in m.post_window1('lemmas')) else 0
    # #19
    # def LF_demonstrate(m):
    #     return 1 if ('demonstrate' in m.post_window1('lemmas')) else 0
    # #20
    # def LF_reveal(m):
    #     return 1 if ('reveal' in m.post_window1('lemmas')) else 0
    # #21
    # def LF_suggest(m):
    #     return 1 if ('suggest' in m.post_window1('lemmas')) else 0
    # #22
    # def LF_evidence(m):
    #     return 1 if ('evidence for' in m.post_window1('lemmas')) else 0
    # #23
    # def LF_indication(m):
    #     return 1 if ('indication of' in m.post_window1('lemmas')) else 0
    # #24
    # def LF_elevation(m):
    #     return 1 if ('elevation' in m.post_window1('lemmas')) else 0
    # #25
    # def LF_diagnosis(m):
    #     return 1 if ('diagnosis of' in m.post_window1('lemmas')) else 0
    # #26
    # def LF_variation(m):
    #     return 1 if ('variation of' in m.pre_window1('lemmas')) else 0
    # #27
    # def LF_modification(m):
    #     return 1 if ('modification of' in m.pre_window1('lemmas')) else 0
    # #28
    # def LF_suggestion(m):
    #     return 1 if ('suggestion' in m.post_window1('lemmas')) else 0
    #
    # # 29
    # def LF_link(m):
    #     return 1 if ('link' in m.post_window1('lemmas')) else 0
    #
    # # 30
    # def LF_derivation(m):
    #     return 1 if ('derivation of' in m.pre_window1('lemmas')) else 0
    #
    # # 31
    # def LF_denote(m):
    #     return 1 if ('denote' in m.post_window1('lemmas')) else 0
    #
    # # 32
    # def LF_denotation(m):
    #     return 1 if ('denotation' in m.post_window1('lemmas')) else 0
    #
    # # 33
    # def LF_demonstration(m):
    #     return 1 if ('demonstration' in m.post_window1('lemmas')) else 0
    #
    # # 34
    # def LF_magnification(m):
    #     return 1 if ('magnification' in m.pre_window1('lemmas')) else 0
    #
    # # 35
    # def LF_depression(m):
    #     return 1 if ('depression' in m.pre_window1('lemmas')) else 0
    #
    # # 36
    # def LF_boost(m):
    #     return 1 if ('boost' in m.pre_window1('lemmas')) else 0
    #
    # # 37
    # def LF_level(m):
    #     return 1 if ('level' in m.pre_window1('lemmas')) else 0
    #
    # # 38
    # def LF_advance(m):
    #     return 1 if ('advance' in m.pre_window1('lemmas')) else 0
    #
    # # 39
    # def LF_augmentation(m):
    #     return 1 if ('augmentation' in m.pre_window1('lemmas')) else 0
    #
    # # 40
    # def LF_decline(m):
    #     return 1 if ('decline' in m.pre_window1('lemmas')) else 0
    #
    # # 41
    # def LF_lessening(m):
    #     return 1 if ('lessening' in m.pre_window1('lemmas')) else 0
    #
    # # 42
    # def LF_enhancement(m):
    #     return 1 if ('enhancement' in m.pre_window1('lemmas')) else 0
    #
    # # 43
    # def LF_expression(m):
    #     return 1 if ('expression' in m.post_window1('lemmas')) else 0
    #
    # # 44
    # def LF_buildup(m):
    #     return 1 if ('buildup' in m.pre_window1('lemmas')) else 0
    #
    # # 45
    # def LF_diminishing(m):
    #     return 1 if ('diminishing' in m.pre_window1('lemmas')) else 0
    #
    # # 46
    # def LF_diminishment(m):
    #     return 1 if ('diminishment' in m.pre_window1('lemmas')) else 0
    #
    # # 47
    # def LF_reduction(m):
    #     return 1 if ('reduction' in m.pre_window1('lemmas')) else 0
    #
    # # 48
    # def LF_drop(m):
    #     return 1 if ('drop' in m.pre_window1('lemmas')) else 0
    #
    # # 49
    # def LF_dwindling(m):
    #     return 1 if ('dwindling' in m.pre_window1('lemmas')) else 0
    #
    # # 50
    # def LF_lowering(m):
    #     return 1 if ('lowering' in m.pre_window1('lemmas')) else 0
    #51
    def LF_possible(m):
        return -1 if ('possible' in m.pre_window1('lemmas')) else 0
    #52
    def LF_explore(m):
        return -1 if ('explore' in m.pre_window1('lemmas')) else 0
    
    # 53
    def LF_key(m):
        # print m.pre_window1('lemmas')
        return -1 if ('abbreviation' in m.pre_window1('lemmas') or (
        'word' in m.pre_window1('lemmas') and 'key' in m.pre_window1('lemmas'))) else 0

    # 54
    def LF_investigate(m):
        return -1 if ('investigate' in m.pre_window1('lemmas')) else 0

    # 55
    def LF_yetToBeConfirmed(m):
        return -1 if ('yet' in m.post_window1('lemmas') and 'to' in m.post_window1('lemmas') and 'be' in m.post_window1('lemmas') and 'confirmed' in m.post_window1('lemmas')) else 0

    # 56
    def LF_notAssociated(m):
        return -1 if ('not' in m.post_window1('lemmas') and 'associated' in m.post_window('lemmas')) else 0

    # 56
    def LF_notRelated(m):
        return -1 if ('not' in m.post_window1('lemmas') and 'related' in m.post_window('lemmas')) else 0

    # 57
    def LF_doesNotShow(m):
        return -1 if ('does' in m.post_window1('lemmas') and 'not' in m.post_window1('lemmas') and 'show' in m.post_window('lemmas')) else 0

    # 58
    def LF_notLinked(m):
        return -1 if ('not' in m.post_window1('lemmas') and 'linked' in m.post_window('lemmas')) else 0

    # 59
    def LF_notCorrelated(m):
        return -1 if ('not' in m.post_window1('lemmas') and 'correlated' in m.post_window('lemmas')) else 0

    # 60
    def LF_disprove(m):
        return -1 if ('disprove' in m.post_window('lemmas')) else 0

    # 61
    def LF_refute(m):
        return -1 if ('disprove' in m.post_window('lemmas')) else 0

    # 62
    def LF_doesNotSignify(m):
        return -1 if ('does' in m.post_window1('lemmas') and 'not' in m.post_window1('lemmas') and 'signify' in m.post_window('lemmas')) else 0

    # 63
    def LF_doesNotIndicate(m):
        return -1 if ('does' in m.post_window1('lemmas') and 'not' in m.post_window1('lemmas') and 'indicate' in m.post_window('lemmas')) else 0

     # 64
    def LF_doesNotImply(m):
        return -1 if ('does' in m.post_window1('lemmas') and 'not' in m.post_window1('lemmas') and 'imply' in m.post_window('lemmas')) else 0

    LFs = [LF_investigate, LF_key, LF_possible, LF_explore, LF_distance, LF_keyword,
           LF_possible, LF_explore, LF_key, LF_investigate, LF_yetToBeConfirmed, LF_notAssociated, LF_notRelated,
           LF_doesNotShow, LF_notLinked, LF_notCorrelated, LF_disprove, LF_refute, LF_doesNotSignify,
           LF_doesNotIndicate, LF_doesNotImply]gts = []
    uids = []
    for tuple in mindtaggerToTruth("tags4.tsv"):
        uids.append(tuple[0])
        gts.append(tuple[1])
    otherModel.update_gt(gts, uids=uids)
    otherModel.open_mindtagger(num_sample=100, width='100%', height=1200)
    otherModel.add_mindtagger_tags()

    otherModel.apply_lfs(LFs, clear=False)
    return otherModel
    # """DEBUGGING CODE"""
    # otherModel.open_mindtagger(num_sample=100, width='100%', height=1200)
    # otherModel.add_mindtagger_tags()
    # otherModel.plot_lf_stats()
    #
    # """END"""
    # # with open("thing.xml", "wb") as f:
    #
    # doEverything()
    
def mindtaggerToTruth(filename):
    uids = []
    list =  re.split("[^\\S ]", open(filename).read())
    # print list
    count = 7
    while count < len(list):
        number = 0
        if(list[count + 6] == "true"):
            number = 1
        elif(list[count + 6] == "false"):
            number = -1
        uids.append((list[count + 5] + "::" + list[count + 3] + "::["  + list[count + 4] + ", " +  list[count] + "]::['" + list[count + 1] + "', '" + list[count + 2] + "']", number))
        count += 7
    return uids
