##


import pandas as pd
from githubdata import GithubData
from mirutil.funcs import search_tsetmc
from mirutil.funcs import read_data_according_to_type as rdata


bticks_repo_url = 'https://github.com/imahdimir/d-BaseTicker'
cur_module_repo = 'https://github.com/imahdimir/gov-BaseTicker'

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
  df = rdata(fpn)

  ##
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
  df = df.merge(ldf , how = 'left')

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
  for i , el in enumerate(df1[btic]) :
    print(str(i + 1) + ':"' + el + '",')

  ##
  ok_bts_0 = {
      1  : "آتي1" ,
      2  : "انرژي1" ,
      3  : "انرژي2" ,
      4  : "انرژي3" ,
      5  : "بورس3" ,
      6  : "عسناسنگ2" ,
      7  : "كالا1" ,
      8  : "كالا2" ,
      9  : "كالا3" ,
      10 : "كالا4" ,
      }

  msk = ~ df1[btic].isin(ok_bts_0.values())
  len(msk[msk])

  ##
  assert len(msk[msk]) == 0

  ##
  ptr = '\D+'
  msk = ~ df[btic].str.fullmatch(ptr)
  msk &= df[btic].str[:-1].isin(df[btic])

  df1 = df[msk]

  ##
  for i , el in enumerate(df1[btic]) :
    print(str(i + 1) + ':"' + el + '",')

  ##
  ok_bts_1 = {
      1 : "بورس3" ,
      2 : "عسناسنگ2" ,
      3 : "كالا1" ,
      4 : "كالا2" ,
      5 : "كالا3" ,
      6 : "كالا4" ,
      }

  msk = ~ df1[btic].isin(ok_bts_1.values())
  len(msk[msk])

  ##
  assert len(msk[msk]) == 0

  ##
  ptr = r'.+' + r'ح'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]

  ##
  for i , el in enumerate(df1[btic]) :
    print(str(i + 1) + ':"' + el + '",')

  ##
  ok_bts_2 = {
      1 : "مفتاح" ,
      }

  msk = ~ df1[btic].isin(ok_bts_2.values())
  len(msk[msk])

  ##
  assert len(msk[msk]) == 0

  ##
  ptr = r'ض' + '.+'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]

  ##
  for i , el in enumerate(df1[btic]) :
    print(str(i + 1) + ':"' + el + '",')

  ##
  ok_bts_3 = {
      }

  msk = ~ df1[btic].isin(ok_bts_3.values())
  len(msk[msk])

  ##
  assert len(msk[msk]) == 0

  ##
  ptr = r'ج' + '.+'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]

  ##
  for i , el in enumerate(df1[btic]) :
    print(str(i + 1) + ':"' + el + '",')

  ##
  ok_bts_4 = {
      1 : "جم" ,
      2 : "جم پيلن" ,
      3 : "جنگل شفارود" ,
      4 : "جهرم" ,
      5 : "جوين" ,
      6 : "جوپار" ,
      }

  msk = ~ df1[btic].isin(ok_bts_4.values())
  len(msk[msk])

  ##
  assert len(msk[msk]) == 0

  ##
  df.to_parquet(fpn)

  ##
  commit_msg = 'checked'
  commit_msg += f' by repo: {cur_module_repo}'

  bticks_repo.commit_push(commit_msg)

  ##


  bticks_repo.rmdir()

  ##


##

##