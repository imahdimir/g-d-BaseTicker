##

"""

  """

##

import pandas as pd
from githubdata import GithubDataRepo
from mirutil.funcs import norm_fa_str as norm
from mirutil.funcs import save_df_as_a_nice_xl as sxl


repo_path = 'https://github.com/imahdimir/d-uniq-BaseTickers'
cur_module_repo = 'https://github.com/imahdimir/gov-d-uniq-BaseTickers'

btic = 'BaseTicker'

def main() :

  pass

  ##
  btick_repo = GithubDataRepo(repo_path)
  btick_repo.clone_overwrite_last_version()
  ##
  data_suffix = '.xlsx'
  fpns = btick_repo.return_sorted_list_of_fpns_with_the_suffix(data_suffix)
  fpn = fpns[0]
  ##
  df = pd.read_excel(fpn)
  ##
  df = df[[btic]]
  ##
  df[btic] = df[btic].apply(norm)
  ##
  df = df.sort_values(btic)
  ##
  df = df.drop_duplicates()
  ##
  sxl(df , btick_repo.local_path / 'data.xlsx')
  ##
  commit_msg = 'date changed to .xlsx format'
  commit_msg += f' by repo: {cur_module_repo}'
  btick_repo.commit_and_push_to_github_data_target(commit_msg)
  ##
  btick_repo.rmdir()

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