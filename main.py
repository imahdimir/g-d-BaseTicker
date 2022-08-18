##

"""

  """

##

import pandas as pd
from githubdata import GithubData
from mirutil.funcs import norm_fa_str as norm
from mirutil.funcs import save_as_prq_wo_index as sprq

repo_path = 'imahdimir/d-Unique-BaseTickers-TSETMC'

btic = 'BaseTicker'

def main() :

  pass

  ##
  btick = GithubData(repo_path)
  btick.clone_overwrite_last_version()
  ##
  fpn = btick.data_fps[0]
  ##
  df = pd.read_parquet(fpn)
  ##
  df = df.reset_index(drop = False)
  ##
  df = df.applymap(norm)
  ##
  df = df.drop_duplicates()
  ##
  df = df.sort_values(btic)
  ##
  df = df.set_index(btic)
  ##
  sprq(df , fpn)
  ##
  btick.commit_and_push_to_github_data_target('now BaseTicker is index column')
  ##
  btick.rmdir()

  ##


  ##

##


# noinspection PyUnreachableCode
if False :

  pass

  ##
  from mirutil.funcs import save_df_as_a_nice_xl as sxl


  ##
  sxl(df , 'd.xlsx')

  ##

##

# noinspection PyUnreachableCode
if False :

  pass

  ##


  ptr = '\D+'
  msk = ~ df[btic].str.fullmatch(ptr)
  df1 = df[msk]
  ##
  ptr = '\D+'
  msk = ~ df[btic].str.fullmatch(ptr)
  msk &= df[btic].str[:-1].isin(df[btic])

  df1 = df[msk]
  # sxl(df1, 'df1.xlsx')
  # df = df[~ msk]
  ##
  ptr = r'.+' + r'ح'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]
  ##
  ptr = r'ض' + '.+'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]
  ##
  ptr = r'ج' + '.+'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]

  ##

##