##

"""

  """
##

import pandas as pd
from githubdata import GithubData
from mirutil.funcs import save_df_as_a_nice_xl as sxl
from mirutil.funcs import search_tsetmc


bticks_repo_url = 'https://github.com/imahdimir/d-uniq-BaseTickers'
cur_module_repo = 'https://github.com/imahdimir/gov-d-uniq-BaseTickers'

btic = 'BaseTicker'
tick = 'Ticker'

listed = 'listed'

def is_base_ticker_on_tsetmc(basetick) :
  df = search_tsetmc(basetick)
  df[tick] = df[tick].str.strip()
  return df[tick].eq(basetick).any()

def main() :
  pass

  ##


  bticks_repo = GithubData(bticks_repo_url)
  bticks_repo.clone()
  ##
  fpn = bticks_repo.data_filepath
  ##
  df = pd.read_excel(fpn)
  ##
  df = df.reset_index()
  df = df[[btic]]
  ##
  df[btic] = df[btic].str.strip()
  ##
  df = df.sort_values(btic)
  ##
  df = df.drop_duplicates()
  ##
  ldf = pd.read_excel('listed.xlsx')
  ##
  df = df.merge(ldf, how = 'left')
  ##
  msk = df[listed].isna()
  len(msk[msk])
  ##
  df.loc[msk , listed] = df.loc[msk , btic].apply(is_base_ticker_on_tsetmc)
  ##
  msk = df[listed].ne(True)
  df.loc[msk , listed] = df.loc[msk , btic].apply(is_base_ticker_on_tsetmc)
  ##
  assert df[listed].all()

  ##
  df = df[[btic]]

  ##
  ptr = '\D+'
  msk = ~ df[btic].str.fullmatch(ptr)
  df1 = df[msk]
  ##
  for el in df1[btic] :
    print('"' + el + '":None,')
  ##
  ok_bts_0 = {
      "آتي1"   : None ,
      "انرژي1" : None ,
      "انرژي2" : None ,
      "انرژي3" : None ,
      "بورس3"  : None ,
      "كالا1"  : None ,
      "كالا2"  : None ,
      "كالا3"  : None ,
      "كالا4"  : None ,
      }

  msk = ~ df1[btic].isin(ok_bts_0)
  len(msk[msk])
  ##
  assert len(msk[msk]) == 0

  ##
  ptr = '\D+'
  msk = ~ df[btic].str.fullmatch(ptr)
  msk &= df[btic].str[:-1].isin(df[btic])

  df1 = df[msk]
  ##
  ok_bts_1 = {
      "بورس3" : None ,
      "كالا1" : None ,
      "كالا2" : None ,
      "كالا3" : None ,
      "كالا4" : None ,
      }

  msk = ~ df1[btic].isin(ok_bts_1)
  len(msk[msk])
  ##
  assert len(msk[msk]) == 0

  ##
  ptr = r'.+' + r'ح'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]

  ##
  ok_bts_2 = {
      "مفتاح" : None ,
      }

  msk = ~ df1[btic].isin(ok_bts_2)
  len(msk[msk])
  ##
  assert len(msk[msk]) == 0

  ##
  ptr = r'ض' + '.+'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]
  ##
  ok_bts_3 = {
      }

  msk = ~ df1[btic].isin(ok_bts_3)
  len(msk[msk])
  ##
  assert len(msk[msk]) == 0

  ##
  ptr = r'ج' + '.+'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]
  ##
  ok_bts_4 = {
      "جم"          : None ,
      "جم پيلن"     : None ,
      "جنگل شفارود" : None ,
      "جهرم"        : None ,
      "جوين"        : None ,
      }

  msk = ~ df1[btic].isin(ok_bts_4)
  len(msk[msk])
  ##
  assert len(msk[msk]) == 0

  ##
  st = 'پذیره'
  msk = df[btic].str.contains(st)
  df1 = df[msk]
  ##
  ok_bts_5 = {
      }

  msk = ~ df1[btic].isin(ok_bts_5)
  len(msk[msk])
  ##
  assert len(msk[msk]) == 0

  ##
  sxl(df , fpn)
  ##
  commit_msg = ''
  commit_msg += f' by repo: {cur_module_repo}'

  bticks_repo.commit_push(commit_msg)
  ##
  bticks_repo.rmdir()

  ##

##