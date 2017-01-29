# -*- coding: utf-8 -*-

# Transform word into transcription
# Rules from http://fonetica.philol.msu.ru/

import rhyme_detect

class Transcription():
    def __init__(self):
        self.all_vowels = [u'а', u'о', u'у', u'э', u'ы', u'и', u'е', u'ю', u'я', u'ё']
        self.jot_vowels = {u'ю': u'у', u'я': u'а', u'е': u'е', u'ё': u'о'}
        self.all_cons = [u'б', u'в', u'г', u'д', u'ж', u'з', u'й', u'j', u'к', u'л', u'м', u'н', u'п',
                         u'р', u'с', u'т', u'ф', u'х', u'ц', u'ш', u'щ', u'ч'] # j is needed for transcription
        self.voiced_cons = {u'б': u'п', u'в': u'ф', u'г': u'к', u'д': u'т', u'ж': u'ш', u'з': u'с'}
        self.pairing_cons = [u'б', u'в', u'г', u'д', u'з', u'к', u'л', u'м', u'н', u'п',
                             u'р', u'с', u'т', u'ф', u'х']
        self.hard_hushing_cons = [u'ш', u'ж', u'ц']
        self.soft_hushing_cons = [u'ч', u'щ']
        self.apply_first_reduction = False
        self.apply_other_pre_reduction = False
        self.apply_post_reduction = False
        self.yo_words = []
        self.shn_words = frozenset([u'конечно', u'скучн', u'нарочн', u'яичниц,'
                          u'прачечн', u'скворечн', u'девичн', u'горчичн'])  # better to have bigger list
        self.hard_de_words = frozenset([u'декольте', u'дельта', u'дендрари', u'дефиле',
                             u'детектор', u'детектив', u'диадема', u'тенденци',
                             u'цитадель',  u'шедевр',  u'рандеву', u'денди'])
        self.hard_te_words = frozenset([u'антитез',  u'тезис',  u'гротеск',  u'интенсив',
                              u'метрополитен', u'патети', u'бутерброд',  u'контейнер',
                              u'теннис',  u'пастель',  u'синтети',  u'альтерна',
                              u'сентенци',  u'тенденци', u'коктейл',  u'штепсел',
                              u'компьютер', u'кортеж', u'ателье', u'свитер',
                              u'пастеризован', u'принтер', u'лотере', u'эстет',
                              u'претен', u'протекци', u'интер', u'тент'])
        self.hard_ze_words = frozenset([u'безе', u'зеро', u'кузен', u'морзе', u'экзем'])
        self.hard_se_words = frozenset([u'антисепт', u'диспансер',  u'нонсенс',  u'сенсор',
                              u'плиссе',  u'фрикасе', u'эссе'])
        self.hard_re_words = frozenset([u'регби',  u'реквием',  u'кабаре',  u'пюре',  u'тире'])
        self.hard_ne_words = frozenset([u'бизнес', u'генез', u'анестези', u'генет',
                              u'майонез', u'полонез', u'тоннел', u'пенсне', u'энерги'])
        self.hard_pe_words = frozenset([u'капелл'])
        self.hard_fe_words = frozenset([u'галифе', u'кафе'])
        self.pre_vowels = []
        self.word_vowels = []
        self.word_consonants = []
        self.stress = 0
        self.word = ''
        self.transcription = ''

    def pre(self, flag):
        rhyme_detect.assign(self)
        if u'ё' not in self.transcription:
            rhyme_detect.yo_words_create(self)
            rhyme_detect.orfo_check(self) #-- becomes very slowly
            if flag == 1:
                rhyme_detect.yo_replace(self)
        else:
            if u'`' not in self.transcription and u'̀' not in self.transcription:
                self.transcription = self.transcription.replace(u'ё', u'ё`')
        rhyme_detect.assimilation(self)
        rhyme_detect.cons_substitutions(self)
        rhyme_detect.jot_vowels_substitution(self)
        rhyme_detect.delete_icts(self)

    def vowels(self):
        rhyme_detect.apply_reductions(self)
        #rhyme_detect.hiatus(self) -- often works not correctly
        if self.apply_other_pre_reduction:
           rhyme_detect.other_pre_stress_reduction(self)
        if self.apply_first_reduction:
            rhyme_detect.first_pre_stress_reduction(self)
        if self.apply_post_reduction:
            rhyme_detect.post_reduction(self)
        self.transcription = self.transcription.lower()
        rhyme_detect.after_hard_hushing(self)
        #for i in range(len(self.transcription)-1):
        #    if self.transcription[i] in self.pairing_cons and self.transcription[i+1] == u'ь':
        #         self.transcription = ''.join(self.transcription[:i+1] + u'\'' + self.transcription[i+2:])

    def consonants(self):
        rhyme_detect.voiceless(self)
        rhyme_detect.simplification(self)

    def transform(self, flag):
        self.pre(flag)
        self.vowels()
        self.consonants()
        if u'ё' in self.transcription:
            self.transcription = self.transcription.replace(u'ё', u'о')
        for sound in self.transcription:
            if sound in self.all_cons or sound == u'j':
                self.word_consonants.append(sound)
            if sound in self.all_vowels or sound in u'ьъ':
                self.word_vowels.append(sound)


#word1 = u'безнаде`жной'
#t = Transcription()
#t.word = word1
#t.transform(1)
#print t.word
#print t.transcription


