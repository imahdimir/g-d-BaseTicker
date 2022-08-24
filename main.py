##

"""

  """
##

import pandas as pd
from githubdata import GithubData
from mirutil.funcs import norm_fa_str as norm
from mirutil.funcs import save_df_as_a_nice_xl as sxl
from mirutil.funcs import read_data_according_to_type as rdata


bticks_repo_url = 'https://github.com/imahdimir/d-uniq-BaseTickers'
cur_module_repo = 'https://github.com/imahdimir/gov-d-uniq-BaseTickers'

btic = 'BaseTicker'

def main() :


  pass

  ##
  bticks_repo = GithubData(bticks_repo_url)
  bticks_repo.clone()
  ##
  fpn = bticks_repo.data_filepath
  ##
  df = rdata(fpn)
  ##
  df = df.reset_index()
  df = df[[btic]]
  ##
  df[btic] = df[btic].apply(norm)
  ##
  df = df.sort_values(btic)
  ##
  df = df.drop_duplicates()
  ##
  sxl(df , fpn)
  ##
  commit_msg = 'applied'
  commit_msg += f' by repo: {cur_module_repo}'

  bticks_repo.commit_push(commit_msg)
  ##
  bticks_repo.rmdir()

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