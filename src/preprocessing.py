def clean_data(df):
    """
    Cleans the merged TMDB movie dataset by:
    - Dropping irrelevant columns
    - Handling missing values
    - Renaming columns
    - Removing duplicate records

    Parameters:
        df (pd.DataFrame): Raw merged DataFrame

    Returns:
        pd.DataFrame: Cleaned DataFrame
    """
    # 1. Drop columns not needed for modeling
    df.drop(columns=['homepage', 'tagline', 'status', 'title_y'], inplace=True, errors='ignore')

    # 2. Fill missing overviews with placeholder
    if 'overview' in df.columns:
        df['overview'].fillna("No overview", inplace=True)

    # 3. Drop rows with missing release_date
    df.dropna(subset=['release_date'], inplace=True)

    # 4. Fill missing runtimes with median
    if 'runtime' in df.columns:
        median_runtime = df['runtime'].median()
        df['runtime'].fillna(median_runtime, inplace=True)

    # 5. Rename 'title_x' to just 'title'
    if 'title_x' in df.columns:
        df.rename(columns={'title_x': 'title'}, inplace=True)

    # 6. Drop duplicate rows and duplicate titles
    df.drop_duplicates(inplace=True)
    df.drop_duplicates(subset='title', keep='first', inplace=True)

    return df
