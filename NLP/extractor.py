import os
import re
from pyltp import SentenceSplitter
from pyltp import Segmentor


# 长句切分。将段落分句，将一段话或一篇文章中的文字按句子分开，按句子形成独立的单元。返回切分好的句子列表
def get_sentences(content):
    # 消去句子中的空格以及换行
    content = content.replace(' ', '').replace('\n', '')
    sents = SentenceSplitter.split(content)
    sents_list = list(sents)
    return sents_list


# 短句切分。将长句按逗号和顿号切分为短句。返回切分好的短句列表
def get_subsents(sentence):
    subsents_list = list()
    subsents = re.split(r'[，：,:]', sentence)
    # 消去长度为0的子句，并将子句加入列表中
    for subsent in subsents:
        if subsent:
            subsents_list.append(subsent)
    return subsents_list


# pyltp分词。
def get_words(sent):
    cws_model_path = os.path.join(os.path.dirname(__file__), 'ltp_data_v3.4.0/cws.model')  # 分词模型路径，模型名称为`cws.model`
    lexicon_path = os.path.join(os.path.dirname(__file__), 'ltp_data_v3.4.0/lexicon.txt')  # 参数lexicon是自定义词典的文件路径

    print('\n' + cws_model_path + '\n')

    print(sent)
    segmentor = Segmentor()

    segmentor.load_with_lexicon(cws_model_path, lexicon_path)

    words = segmentor.segment(sent)  # 分词

    # print('/'.join(words))

    segmentor.release()

    return words


# 处理段落content
def process_content(content):
    sentences = get_sentences(content)
    print('\n'.join(sentences))
    print('\n')
    subsents = list()
    for sentence in sentences:
        subsents = get_subsents(sentence)
        print(' / '.join(subsents))

    print('/'.join(get_words(subsents[0])))

    return


def main():
    test_content = '''
    据韩联社12月28日反映，美国
        防部发言人杰夫·莫莱尔27日表示：美国防部长盖 茨将
    于2011年1月14日访问韩国。盖茨原计划从   
    
    明年1月9日至14日陆续访问中国和日本，目前，他决定在行程     
    中增加对韩国的访问;莫莱尔表示，盖茨在访韩期间将会晤韩国国
    防部长官金宽镇，就朝鲜近日的行动交换意见，同时商讨加强韩美两军同盟关系等问题，
    拟定共同应对朝鲜挑衅和核计划的方案。
    '''
    test_content2 = '''
        测试文件是根据粒度和(长短句)的大小所编写得特殊句子：分别为这个东西、那个东西以及另外一些东西？
    他们来了；我们也来了；都来了。
    '''
    test_content3 = '''
    公安部近日组织全国公安机关开展扫黑除恶
    追逃“清零”行动。公安部将1712名涉黑涉恶
    逃犯列为“清零”行动目标逃犯，逐一明确追
    逃责任人，实行挂账督捕，并对13名重点在
    逃人员发布A级通缉令↓见到这些人请报警，
    转发扩散！
    '''
    process_content(test_content3)
    return


if __name__ == '__main__':
    main()